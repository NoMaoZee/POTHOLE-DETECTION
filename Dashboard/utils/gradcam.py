"""
Grad-CAM implementation for XAI
Generates visual explanations for model predictions
"""

import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import Model

def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    """
    Generate Grad-CAM heatmap
    
    Args:
        img_array: Preprocessed image array
        model: Trained model
        last_conv_layer_name: Name of last conv layer
        pred_index: Class index (None = use predicted class)
    
    Returns:
        heatmap: Numpy array of heatmap
    """
    # Get the last convolutional layer
    try:
        last_conv_layer = model.get_layer(last_conv_layer_name)
    except:
        # Try to find the last conv layer automatically
        for layer in reversed(model.layers):
            if 'conv' in layer.name.lower():
                last_conv_layer = layer
                break
        else:
            raise ValueError(f"No convolutional layer found in model")
    
    # Create gradient model
    grad_model = Model(
        inputs=[model.input],
        outputs=[last_conv_layer.output, model.output]
    )
    
    # Compute gradient
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        
        if pred_index is None:
            pred_index = tf.argmax(predictions[0])
        
        class_channel = predictions[:, pred_index]
    
    # Compute gradients
    grads = tape.gradient(class_channel, conv_outputs)
    
    # Global average pooling
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    # Weight the channels
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    
    # Normalize
    heatmap = tf.maximum(heatmap, 0) / (tf.reduce_max(heatmap) + 1e-8)
    
    return heatmap.numpy()

def generate_gradcam_overlay(pil_image, heatmap, alpha=0.4):
    """
    Generate Grad-CAM overlay on original image
    
    Args:
        pil_image: Original PIL image
        heatmap: Grad-CAM heatmap
        alpha: Overlay transparency
    
    Returns:
        heatmap_img: Colored heatmap
        overlay: Overlay image
    """
    # Convert PIL to numpy
    img = np.array(pil_image.convert("RGB"))
    
    # Resize heatmap to match image
    heatmap_resized = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap_resized = np.uint8(255 * heatmap_resized)
    
    # Apply colormap
    heatmap_color = cv2.applyColorMap(heatmap_resized, cv2.COLORMAP_JET)
    heatmap_color = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2RGB)
    
    # Create overlay
    overlay = cv2.addWeighted(heatmap_color, alpha, img, 1 - alpha, 0)
    
    return heatmap_resized, overlay

def predict_with_gradcam(model, pil_image, class_names, last_conv_layer, 
                         model_type="PureCNN"):
    """
    Combined prediction + Grad-CAM generation
    
    Args:
        model: Trained model
        pil_image: PIL Image
        class_names: List of class names
        last_conv_layer: Name of last conv layer
        model_type: Type of model for preprocessing
    
    Returns:
        pred_label: Predicted class
        pred_conf: Confidence score
        preds: All class probabilities
        heatmap: Grad-CAM heatmap
        overlay: Overlay image
    """
    from .inference import (preprocess_image_purecnn, 
                           preprocess_image_resnet, 
                           preprocess_image_efficientnet)
    
    # Preprocess based on model type
    if model_type == "PureCNN":
        img_array = preprocess_image_purecnn(pil_image)
    elif model_type == "ResNet50":
        img_array = preprocess_image_resnet(pil_image)
    else:
        img_array = preprocess_image_efficientnet(pil_image)
    
    # Predict
    preds = model.predict(img_array, verbose=0)[0]
    pred_idx = np.argmax(preds)
    pred_label = class_names[pred_idx]
    pred_conf = preds[pred_idx]
    
    # Generate Grad-CAM
    try:
        heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer, pred_index=pred_idx)
        heatmap_img, overlay = generate_gradcam_overlay(pil_image, heatmap)
    except Exception as e:
        print(f"Grad-CAM generation failed: {e}")
        # Return dummy heatmap if fails
        heatmap = np.zeros((7, 7))
        heatmap_img = np.zeros((224, 224))
        overlay = np.array(pil_image.convert("RGB"))
    
    return pred_label, pred_conf, preds, heatmap, overlay