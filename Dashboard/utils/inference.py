"""
Inference utilities for predictions
Handles image preprocessing and predictions
"""

import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.applications.efficientnet import preprocess_input as efficient_preprocess

def preprocess_image_purecnn(pil_image, target_size=(224, 224)):
    """Preprocess for PureCNN - simple normalization"""
    img = pil_image.convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def preprocess_image_resnet(pil_image, target_size=(224, 224)):
    """Preprocess for ResNet50"""
    img = pil_image.convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = resnet_preprocess(img_array)
    return img_array

def preprocess_image_efficientnet(pil_image, target_size=(224, 224)):
    """Preprocess for EfficientNet"""
    img = pil_image.convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = efficient_preprocess(img_array)
    return img_array

def predict_image(model, pil_image, class_names, model_type="PureCNN"):
    """Run prediction on single image"""
    # Choose preprocessing based on model type
    if model_type == "PureCNN":
        img_array = preprocess_image_purecnn(pil_image)
    elif model_type == "ResNet50":
        img_array = preprocess_image_resnet(pil_image)
    else:  # EfficientNet
        img_array = preprocess_image_efficientnet(pil_image)
    
    # Predict
    preds = model.predict(img_array, verbose=0)[0]
    pred_idx = np.argmax(preds)
    pred_label = class_names[pred_idx]
    pred_conf = preds[pred_idx]
    
    return pred_label, pred_conf, preds

def compute_image_stats(pil_image):
    """Compute image statistics for EDA"""
    img_array = np.array(pil_image.convert("RGB"))
    
    stats = {
        "width": pil_image.size[0],
        "height": pil_image.size[1],
        "channels": img_array.shape[2] if len(img_array.shape) == 3 else 1,
        "mean_brightness": float(np.mean(img_array)),
        "std_brightness": float(np.std(img_array)),
        "min_pixel": int(np.min(img_array)),
        "max_pixel": int(np.max(img_array)),
        "format": pil_image.format if pil_image.format else "Unknown"
    }
    
    return stats

def generate_interpretation(pred_label, pred_conf, model_name):
    """Generate text interpretation of prediction"""
    
    if pred_label == "POTHOLE":
        base_text = f"""
### <i class="fa-solid fa-exclamation-triangle"></i> Pothole Detected!

The **{model_name}** model has identified a **POTHOLE** in this image with **{pred_conf:.1%}** confidence.

**What the model sees:**
- Visible cracks or holes in the road surface
- Damaged asphalt patterns
- Irregular surface textures
- Depth variations indicating road deterioration

**Recommendation:**
- This section requires immediate inspection
- Potential risk for vehicle damage
- Consider marking for maintenance priority
"""
    else:
        base_text = f"""
### <i class="fa-solid fa-check-circle"></i> Clean Road Surface

The **{model_name}** model has classified this as **NO POTHOLE** with **{pred_conf:.1%}** confidence.

**What the model sees:**
- Smooth asphalt surface
- No visible cracks or holes
- Well-maintained road condition
- Uniform surface texture

**Status:**
- Road appears to be in good condition
- No immediate maintenance required
- Continue regular monitoring
"""
    
    # Add confidence warning if low
    if pred_conf < 0.7:
        base_text += f"""

<i class="fa-solid fa-exclamation-circle"></i> **Note:** The model's confidence is relatively low ({pred_conf:.1%}). 
Consider additional verification for this image.
"""
    
    return base_text