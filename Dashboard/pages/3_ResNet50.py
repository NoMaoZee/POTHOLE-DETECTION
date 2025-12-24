"""
ResNet50 Model Page - Purple + Black Theme
Transfer Learning Architecture - 99.16% Accuracy
"""

import streamlit as st
import os
import sys
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import zipfile

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import (
    get_base_css, get_resnet_theme,
    load_resnet_model, get_model_info, CLASS_NAMES,
    predict_with_gradcam, compute_image_stats, generate_interpretation
)

# Page config
st.set_page_config(
    page_title="ResNet50 - Pothole Detection",
    page_icon="🟣",
    layout="wide"
)

# Apply styling
st.markdown(get_base_css(), unsafe_allow_html=True)
st.markdown(get_resnet_theme(), unsafe_allow_html=True)

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
RESNET_DIR = os.path.join(PROJECT_ROOT, "ResNet50")

# Title
st.markdown("""
<div style="text-align: center; padding: 1.5rem 0;">
    <h1><i class="fa-solid fa-network-wired"></i> Pothole Detection AI - ResNet50</h1>
    <p style="font-size: 20px; background: linear-gradient(90deg, #7B1FA2 0%, #AB47BC 100%); 
       -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700;">
        Transfer Learning Architecture | Silver Medal 🥈
    </p>
</div>
""", unsafe_allow_html=True)

# Load model
model = load_resnet_model()
model_info = get_model_info("ResNet50")

if model is None:
    st.error("Model not found! Please check model path.")
    st.stop()

# Sidebar - Model info
with st.sidebar:
    st.markdown("### <i class='fa-solid fa-info-circle'></i> Model Information", unsafe_allow_html=True)
    st.info(f"""
    **Architecture**: {model_info['architecture']}  
    **Parameters**: {model_info['parameters']}  
    **Input Size**: {model_info['input_size']}  
    **Accuracy**: 99.16%
    """)
    
    st.markdown("---")
    st.markdown("### <i class='fa-solid fa-sliders'></i> Training Config", unsafe_allow_html=True)
    st.code(f"""
Epochs: {model_info['training_epochs']}
Learning Rate: {model_info['learning_rate']}
Optimizer: {model_info['optimizer']}
Batch Size: {model_info['batch_size']}
Strategy: Frozen base + Custom top
    """)

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Model Performance",
    "🔍 Single Image Detection",
    "📷 Real-Time Camera",
    "📦 Batch Analysis"
])

# ===== TAB 1: Model Performance =====
with tab1:
    st.markdown("## <i class='fa-solid fa-chart-bar'></i> Model Performance Dashboard", unsafe_allow_html=True)
    
    # Quick metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Accuracy", "99.16%", "2nd Place")
    with col2:
        st.metric("Precision", "99.16%")
    with col3:
        st.metric("Recall", "99.16%")
    with col4:
        st.metric("F1-Score", "99.16%")
    
    st.markdown("---")
    
    # Training curves
    st.markdown("### <i class='fa-solid fa-chart-line'></i> Training History", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        metrics_img = os.path.join(RESNET_DIR, "Training", "training_metrics.png")
        if os.path.exists(metrics_img):
            st.image(metrics_img, caption="Training Curves", use_container_width=True)
        else:
            st.warning("Training metrics image not found")
    
    with col2:
        cm_img = os.path.join(RESNET_DIR, "Evaluation", "confusion_matrix.png")
        if os.path.exists(cm_img):
            st.image(cm_img, caption="Confusion Matrix", use_container_width=True)
        else:
            st.warning("Confusion matrix not found")
    
    # EDA
    st.markdown("---")
    st.markdown("### <i class='fa-solid fa-chart-pie'></i> Exploratory Data Analysis", unsafe_allow_html=True)
    
    stacked_bar = os.path.join(RESNET_DIR, "EDA", "stacked_bar.png")
    if os.path.exists(stacked_bar):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(stacked_bar, caption="Dataset Distribution", use_container_width=True)
    else:
        st.info("EDA visualizations not found")
    
    # Transfer Learning Info
    st.markdown("---")
    st.markdown("### <i class='fa-solid fa-graduation-cap'></i> Transfer Learning Details", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Base Model: ResNet50
        - **Pre-trained on**: ImageNet (1.2M images)
        - **Layers**: 50 deep layers
        - **Strategy**: Frozen base layers
        - **Fine-tuning**: Only top layers trained
        """)
    
    with col2:
        st.markdown("""
        #### Advantages
        - ✅ Faster convergence
        - ✅ Better generalization
        - ✅ Leverages ImageNet knowledge
        - ✅ Robust feature extraction
        """)

# ===== TAB 2: Single Image Detection =====
with tab2:
    st.markdown("## <i class='fa-solid fa-upload'></i> Upload Image for Detection", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose an image (JPG, PNG, JPEG)",
        type=["jpg", "png", "jpeg"],
        help="Upload a road image to detect potholes"
    )
    
    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)
        
        with st.spinner("Processing image..."):
            # Step 1: Display original
            st.markdown("---")
            st.markdown("### <i class='fa-solid fa-image'></i> Step 1: Original Image", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(pil_image, caption="Uploaded Image", use_container_width=True)
            
            # Step 2: EDA
            st.markdown("---")
            st.markdown("### <i class='fa-solid fa-magnifying-glass-chart'></i> Step 2: Image Analysis", unsafe_allow_html=True)
            
            stats = compute_image_stats(pil_image)
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Width", f"{stats['width']}px")
            col2.metric("Height", f"{stats['height']}px")
            col3.metric("Brightness", f"{stats['mean_brightness']:.1f}")
            col4.metric("Format", stats['format'])
            
            # Step 3: Prediction
            st.markdown("---")
            st.markdown("### <i class='fa-solid fa-bullseye'></i> Step 3: Model Prediction", unsafe_allow_html=True)
            
            pred_label, pred_conf, preds, heatmap, overlay = predict_with_gradcam(
                model, pil_image, CLASS_NAMES, 
                last_conv_layer=model_info['last_conv_layer'],
                model_type="ResNet50"
            )
            
            # Result box
            result_color = "#7B1FA2" if pred_label == "POTHOLE" else "#4CAF50"
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {result_color}22 0%, {result_color}44 100%); 
                        padding: 2rem; border-radius: 12px; border: 2px solid {result_color}; text-align: center;">
                <h2 style="margin: 0; color: {result_color};">
                    <i class="fa-solid fa-{'exclamation-triangle' if pred_label == 'POTHOLE' else 'check-circle'}"></i> 
                    {pred_label}
                </h2>
                <p style="font-size: 24px; margin: 1rem 0 0 0;">
                    Confidence: <strong>{pred_conf:.2%}</strong>
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Probability bar chart
            st.markdown("#### Class Probabilities")
            prob_df = pd.DataFrame({
                "Class": CLASS_NAMES,
                "Probability": preds
            })
            
            fig, ax = plt.subplots(figsize=(8, 3), facecolor='#0f0f0f')
            ax.set_facecolor('#0f0f0f')
            colors = ['#7B1FA2' if c == pred_label else '#4a4a4a' for c in CLASS_NAMES]
            ax.barh(prob_df["Class"], prob_df["Probability"], color=colors)
            ax.set_xlabel("Probability", fontweight='bold', color='white')
            ax.set_title("Prediction Probabilities", fontweight='bold', color='white')
            ax.set_xlim(0, 1)
            ax.tick_params(colors='white')
            for spine in ax.spines.values():
                spine.set_color('white')
            st.pyplot(fig)
            plt.close()
            
            # Step 4: XAI
            st.markdown("---")
            st.markdown("### <i class='fa-solid fa-eye'></i> Step 4: XAI - Grad-CAM Visualization", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.image(pil_image, caption="Original", use_container_width=True)
            
            with col2:
                fig_heat, ax_heat = plt.subplots(facecolor='#0f0f0f')
                ax_heat.imshow(heatmap, cmap='jet')
                ax_heat.axis('off')
                st.pyplot(fig_heat)
                plt.close()
                st.caption("Heatmap")
            
            with col3:
                st.image(overlay, caption="Overlay", use_container_width=True)
            
            # Step 5: Interpretation
            st.markdown("---")
            st.markdown("### <i class='fa-solid fa-comments'></i> Step 5: Model Interpretation", unsafe_allow_html=True)
            
            interpretation = generate_interpretation(pred_label, pred_conf, "ResNet50")
            st.markdown(interpretation, unsafe_allow_html=True)

# ===== TAB 3: Real-Time Camera =====
with tab3:
    st.markdown("## <i class='fa-solid fa-camera'></i> Real-Time Camera Detection", unsafe_allow_html=True)
    st.info("This feature works best when running locally. In deployed version, use image upload instead.")
    
    camera_image = st.camera_input("Take a photo")
    
    if camera_image is not None:
        pil_image = Image.open(camera_image)
        
        with st.spinner("Analyzing..."):
            pred_label, pred_conf, preds, heatmap, overlay = predict_with_gradcam(
                model, pil_image, CLASS_NAMES,
                last_conv_layer=model_info['last_conv_layer'],
                model_type="ResNet50"
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(pil_image, caption="Captured Image", use_container_width=True)
            
            with col2:
                st.image(overlay, caption="Grad-CAM Overlay", use_container_width=True)
            
            result_color = "#7B1FA2" if pred_label == "POTHOLE" else "#4CAF50"
            st.markdown(f"""
            <div style="background: {result_color}22; padding: 1.5rem; border-radius: 10px; 
                        border-left: 4px solid {result_color}; margin-top: 1rem;">
                <h3 style="margin: 0; color: {result_color};">Result: {pred_label}</h3>
                <p style="margin: 0.5rem 0 0 0;">Confidence: {pred_conf:.2%}</p>
            </div>
            """, unsafe_allow_html=True)

# ===== TAB 4: Batch Analysis =====
with tab4:
    st.markdown("## <i class='fa-solid fa-folder-open'></i> Batch Image Analysis", unsafe_allow_html=True)
    
    uploaded_zip = st.file_uploader("Upload ZIP file containing images", type=["zip"])
    
    if uploaded_zip is not None:
        images = []
        image_names = []
        
        with zipfile.ZipFile(uploaded_zip, 'r') as z:
            for fname in z.namelist():
                if fname.lower().endswith(('.jpg', '.png', '.jpeg')):
                    with z.open(fname) as f:
                        images.append(Image.open(BytesIO(f.read())).copy())
                        image_names.append(os.path.basename(fname))
        
        if len(images) > 0:
            st.success(f"✅ {len(images)} images loaded successfully!")
            
            if st.button("🚀 Start Batch Analysis", use_container_width=True):
                progress_bar = st.progress(0)
                results = []
                
                for idx, (img, name) in enumerate(zip(images, image_names)):
                    from utils.inference import predict_image
                    pred_label, pred_conf, preds = predict_image(
                        model, img, CLASS_NAMES, model_type="ResNet50"
                    )
                    results.append({
                        "image_name": name,
                        "prediction": pred_label,
                        "confidence": pred_conf,
                        "prob_nopothole": preds[0],
                        "prob_pothole": preds[1]
                    })
                    progress_bar.progress((idx + 1) / len(images))
                
                df_results = pd.DataFrame(results)
                
                # Results table
                st.markdown("---")
                st.markdown("### <i class='fa-solid fa-table'></i> Batch Results", unsafe_allow_html=True)
                st.dataframe(df_results, use_container_width=True)
                
                # Statistics
                st.markdown("---")
                st.markdown("### <i class='fa-solid fa-chart-pie'></i> Batch Statistics", unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### Prediction Distribution")
                    class_counts = df_results["prediction"].value_counts()
                    
                    fig1, ax1 = plt.subplots(figsize=(6, 4), facecolor='#0f0f0f')
                    ax1.set_facecolor('#0f0f0f')
                    ax1.bar(class_counts.index, class_counts.values, 
                           color=['#7B1FA2', '#4CAF50'])
                    ax1.set_ylabel("Count", fontweight='bold', color='white')
                    ax1.set_title("Predictions", fontweight='bold', color='white')
                    ax1.tick_params(colors='white')
                    for spine in ax1.spines.values():
                        spine.set_color('white')
                    st.pyplot(fig1)
                    plt.close()
                
                with col2:
                    st.markdown("#### Confidence Distribution")
                    fig2, ax2 = plt.subplots(figsize=(6, 4), facecolor='#0f0f0f')
                    ax2.set_facecolor('#0f0f0f')
                    ax2.hist(df_results["confidence"], bins=10, 
                            color='#7B1FA2', edgecolor='white')
                    ax2.set_xlabel("Confidence", fontweight='bold', color='white')
                    ax2.set_ylabel("Frequency", fontweight='bold', color='white')
                    ax2.set_title("Confidence Scores", fontweight='bold', color='white')
                    ax2.tick_params(colors='white')
                    for spine in ax2.spines.values():
                        spine.set_color('white')
                    st.pyplot(fig2)
                    plt.close()
                
                # Download results
                csv = df_results.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results (CSV)",
                    data=csv,
                    file_name="resnet50_batch_results.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        else:
            st.warning("No valid images found in ZIP file")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 2rem 0;">
    <p style="margin: 0; font-size: 14px;">
        <i class="fa-solid fa-copyright"></i> 2024 Zeedan Mustami Argani | University of Muhammadiyah Malang
    </p>
    <p style="margin: 0.5rem 0 0 0; font-size: 12px; color: #666;">
        <i class="fa-solid fa-network-wired"></i> ResNet50 Model - Transfer Learning Architecture
    </p>
</div>
""", unsafe_allow_html=True)
