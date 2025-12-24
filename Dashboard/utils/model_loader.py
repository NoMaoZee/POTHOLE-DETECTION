"""
Model loading utilities with caching
Loads trained models for inference
"""

import os
import streamlit as st
from tensorflow.keras.models import load_model

# Model paths (relative to Dashboard folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

PURECNN_MODEL = os.path.join(PROJECT_ROOT, "PureCNN", "Model", "final_model_fixed.keras")
RESNET_MODEL = os.path.join(PROJECT_ROOT, "ResNet50", "Model", "resnet50_final_fixed.keras")
EFFICIENT_MODEL = os.path.join(PROJECT_ROOT, "EfficientNet", "Model", "efficientnet_final_fixed.keras")

CLASS_NAMES = ["NOPOTHOLE", "POTHOLE"]

@st.cache_resource
def load_purecnn_model():
    """Load PureCNN model (cached)"""
    if not os.path.exists(PURECNN_MODEL):
        st.error(f"Model not found: {PURECNN_MODEL}")
        return None
    return load_model(PURECNN_MODEL)

@st.cache_resource
def load_resnet_model():
    """Load ResNet50 model (cached)"""
    if not os.path.exists(RESNET_MODEL):
        st.error(f"Model not found: {RESNET_MODEL}")
        return None
    return load_model(RESNET_MODEL)

@st.cache_resource
def load_efficientnet_model():
    """Load EfficientNet model (cached)"""
    if not os.path.exists(EFFICIENT_MODEL):
        st.error(f"Model not found: {EFFICIENT_MODEL}")
        return None
    return load_model(EFFICIENT_MODEL)

def get_model_info(model_name):
    """Get model metadata"""
    model_configs = {
        "PureCNN": {
            "architecture": "Custom CNN (3 Conv + 2 Dense)",
            "input_size": (224, 224, 3),
            "parameters": "~2M",
            "preprocessing": "Simple normalization (÷255)",
            "last_conv_layer": "conv2d_2",
            "training_epochs": 20,
            "learning_rate": 0.001,
            "optimizer": "Adam",
            "batch_size": 32
        },
        "ResNet50": {
            "architecture": "ResNet50 (Transfer Learning)",
            "input_size": (224, 224, 3),
            "parameters": "~23M",
            "preprocessing": "ResNet preprocessing",
            "last_conv_layer": "conv5_block3_out",
            "training_epochs": 15,
            "learning_rate": 0.0001,
            "optimizer": "Adam",
            "batch_size": 32
        },
        "EfficientNet": {
            "architecture": "EfficientNetB0 (Transfer Learning)",
            "input_size": (224, 224, 3),
            "parameters": "~4M",
            "preprocessing": "EfficientNet preprocessing",
            "last_conv_layer": "top_activation",
            "training_epochs": 8,
            "learning_rate": 0.0001,
            "optimizer": "Adam",
            "batch_size": 32
        }
    }
    return model_configs.get(model_name, {})

def check_model_exists(model_name):
    """Check if model file exists"""
    paths = {
        "PureCNN": PURECNN_MODEL,
        "ResNet50": RESNET_MODEL,
        "EfficientNet": EFFICIENT_MODEL
    }
    path = paths.get(model_name)
    return os.path.exists(path) if path else False