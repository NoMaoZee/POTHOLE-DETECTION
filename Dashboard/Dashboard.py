"""
Home Dashboard - Model Comparison
Displays overall performance and comparison from allmodel folder
"""

import streamlit as st
import os
import pandas as pd
import json
from PIL import Image
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.styling import get_base_css, get_home_theme

# Page config
st.set_page_config(
    page_title="Dashboard - Pothole Detection",
    page_icon="🏠",
    layout="wide"
)

# Apply styling
st.markdown(get_base_css(), unsafe_allow_html=True)
st.markdown(get_home_theme(), unsafe_allow_html=True)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Dashboard folder
PROJECT_ROOT = os.path.dirname(BASE_DIR)  # UAP_MachineLearning folder
ALLMODEL_DIR = os.path.join(PROJECT_ROOT, "allmodel")

# ========== SIDEBAR CUSTOM STYLING ==========
# Inject CSS to move title to original top and style the card
st.markdown("""
    <style>
        /* Hide the default navigation links */
        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        [data-testid="stSidebarNav"] + div {
            padding-top: 2rem;
        }
        
        .best-model-card {
            background: rgba(25, 118, 210, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(25, 118, 210, 0.3);
            padding: 20px;
            margin-top: 20px;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        
        .glow-text {
            color: #fff;
            text-shadow: 0 0 10px rgba(25, 118, 210, 0.8), 
                         0 0 20px rgba(25, 118, 210, 0.5);
        }
        
        .stat-box {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# ========== SIDEBAR CONTENT ==========
with st.sidebar:
    # 1. TITLE AT THE VERY TOP
    st.markdown("""
    <div style='text-align: center; padding: 0 0 1.5rem 0; border-bottom: 2px solid #1976D2;'>
        <h2 style='margin: 0; color: #ffffff; font-size: 2.4rem; font-weight: 700; letter-spacing: 1px;'>
            <i class="fa-solid fa-car-burst" style="color: #1976D2;"></i> Pothole AI
        </h2>
        <p style='margin: 5px 0 0 0; font-size: 1rem; color: #888; text-transform: uppercase;'>Real-time Detection System</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. MODEL SELECTION DROPDOWN
    st.markdown("""<p style='margin: 0; font-size: 0.8rem; font-weight: 700; color: #1976D2; text-transform: uppercase;'>Choice Your Model</p>""", unsafe_allow_html=True)
    
    # Define model mapping
    model_options = {
        "Select Model...": None,
        "PureCNN": "pages/2_PureCNN.py",
        "ResNet50": "pages/3_ResNet50.py",
        "EfficientNet": "pages/4_EfficientNet.py"
    }
    
    selected_page = st.selectbox(
        "Choice Your Model",
        options=list(model_options.keys()),
        label_visibility="collapsed"
    )
    
    # Navigation logic
    if selected_page and model_options[selected_page]:
        st.switch_page(model_options[selected_page])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 3. BEST MODEL PREMIUM CARD
    st.markdown("""<div class="best-model-card"><div style='font-size: 0.8rem; font-weight: 700; color: #1976D2; text-transform: uppercase; margin-bottom: 15px;'><i class="fa-solid fa-crown"></i> &nbsp; Best Performance</div><h2 class="glow-text" style='margin: 0; font-size: 1.8rem;'>PureCNN</h2><div style='font-size: 0.9rem; color: #ffd700; margin-bottom: 20px;'>Rank #1 🥇</div><!-- Accuracy Section --><div class="stat-box" style="border: 1px solid rgba(25, 118, 210, 0.5);"><div style='font-size: 0.65rem; color: #42A5F5; text-transform: uppercase; font-weight: 600;'>Overall Accuracy</div><div style='font-size: 1.8rem; font-weight: 800; color: #fff;'>99.49%</div></div><!-- Metrics Grid --><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;"><div class="stat-box"><div style='font-size: 0.55rem; color: #888;'>F1-SCORE</div><div style='font-size: 1rem; font-weight: 700; color: #42A5F5;'>99.5%</div></div><div class="stat-box"><div style='font-size: 0.55rem; color: #888;'>RECALL</div><div style='font-size: 1rem; font-weight: 700; color: #42A5F5;'>99.66%</div></div></div><div class="stat-box" style="margin-top: 10px;"><div style='font-size: 0.55rem; color: #888;'>PRECISION</div><div style='font-size: 1rem; font-weight: 700; color: #42A5F5;'>99.33%</div></div></div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 3. DEVELOPER INFO / FOOTER
    st.markdown("""
    <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.03); border-radius: 10px; border-top: 1px solid #333;'>
        <p style='margin: 0; font-size: 0.75rem; font-weight: 600; color: #fff;'>Zeedan Mustami Argani</p>
        <p style='margin: 2px 0; font-size: 0.65rem; color: #666;'>Univ. Muhammadiyah Malang</p>
        <div style="display: flex; justify-content: center; gap: 10px; margin-top: 8px; color: #1976D2;">
            <i class="fa-brands fa-github"></i>
            <i class="fa-brands fa-linkedin"></i>
            <i class="fa-solid fa-graduation-cap"></i>
        </div>
    </div>
    """, unsafe_allow_html=True)





# Title
st.markdown("""
<div style="text-align: center; padding: 1.5rem 0;">
    <h1><i class="fa-solid fa-chart-line"></i> Overall Dashboard</h1>
    <p style="font-size: 18px; color: #b8b8b8;">
        Comprehensive Model Performance Analysis
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load comparison data
comparison_csv = os.path.join(ALLMODEL_DIR, "comparison.csv")
report_json = os.path.join(ALLMODEL_DIR, "report.json")

if os.path.exists(comparison_csv):
    df_comparison = pd.read_csv(comparison_csv)
    
    # Performance metrics section
    st.markdown("### <i class='fa-solid fa-trophy'></i> Model Performance Comparison", unsafe_allow_html=True)
    
    # Display metrics in cards
    col1, col2, col3 = st.columns(3)
    
    # Define styles for the main dashboard cards
    st.markdown("""
        <style>
            .perf-card {
                background: rgba(255, 255, 255, 0.03);
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                transition: transform 0.3s ease;
                height: 100%;
            }
            .perf-card:hover {
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.05);
            }
            .rank-badge {
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.7rem;
                font-weight: 700;
                display: inline-block;
                margin-top: 10px;
            }
            .metric-val {
                font-size: 1.5rem;
                font-weight: 800;
                margin: 0;
            }
            .metric-lbl {
                font-size: 0.6rem;
                color: #888;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-bottom: 2px;
            }
        </style>
    """, unsafe_allow_html=True)

    for idx, (col, row) in enumerate(zip([col1, col2, col3], df_comparison.itertuples())):
        with col:
            colors = ["#1976D2", "#7B1FA2", "#E65100"]
            medals = ["🥇", "🥈", "🥉"]
            
            st.markdown(f"""<div class="perf-card" style="border-top: 4px solid {colors[idx]}; box-shadow: 0 4px 20px {colors[idx]}22;"><div style="font-size: 2.5rem; margin-bottom: 5px;">{medals[idx]}</div><h3 style="margin: 0; color: {colors[idx]}; font-size: 1.4rem;">{row.Model}</h3><div class="rank-badge" style="background: {colors[idx]}33; color: {colors[idx]};">RANK #{idx+1}</div><div style="margin: 20px 0; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 10px; border: 1px solid {colors[idx]}33;"><div class="metric-lbl">Overall Accuracy</div><div class="metric-val" style="color: {colors[idx]};">{row.Accuracy}</div></div><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;"><div style="padding: 10px; background: rgba(255,255,255,0.02); border-radius: 8px;"><div class="metric-lbl">F1-Score</div><div style="font-size: 1rem; font-weight: 700; color: #fff;">{row._5}</div></div><div style="padding: 10px; background: rgba(255,255,255,0.02); border-radius: 8px;"><div class="metric-lbl">Precision</div><div style="font-size: 1rem; font-weight: 700; color: #fff;">{row.Precision}</div></div></div><div style="margin-top: 10px; padding: 10px; background: rgba(255,255,255,0.02); border-radius: 8px;"><div class="metric-lbl">Recall</div><div style="font-size: 1rem; font-weight: 700; color: #fff;">{row.Recall}</div></div></div>""", unsafe_allow_html=True)

    
    st.markdown("---")
    
    # Detailed comparison table
    st.markdown("### <i class='fa-solid fa-table'></i> Detailed Metrics Table", unsafe_allow_html=True)
    st.dataframe(df_comparison, use_container_width=True, height=200)
    
else:
    st.warning("Comparison data not found. Please ensure training is complete.")

st.markdown("---")

# Visualization gallery
st.markdown("### <i class='fa-solid fa-images'></i> Performance Visualizations", unsafe_allow_html=True)

viz_files = {
    "Performance Bars": "performance_bars.png",
    "Radar Chart": "radar_neon.png",
    "Heatmap": "heatmap_gradient.png",
    "Championship Podium": "podium.png",
    "Ultimate Dashboard": "ultimate_dashboard.png"
}

# Display in tabs
tabs = st.tabs(list(viz_files.keys()))

for tab, (name, filename) in zip(tabs, viz_files.items()):
    with tab:
        img_path = os.path.join(ALLMODEL_DIR, filename)
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, use_container_width=True, caption=name)
        else:
            st.info(f"Visualization '{name}' not found at: {img_path}")

st.markdown("---")

# Model insights
st.markdown("### <i class='fa-solid fa-lightbulb'></i> Key Insights", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### Champion Model: PureCNN
    
    - **Highest Accuracy**: 99.49%
    - **Architecture**: Custom CNN with 3 convolutional layers
    - **Training Time**: 30-45 minutes
    - **Parameters**: ~2M
    
    **Why it wins:**
    - Optimized specifically for pothole detection
    - Lightweight yet powerful architecture
    - Perfect balance of depth and efficiency
    """)

with col2:
    st.markdown("""
    #### Most Efficient: EfficientNet
    
    - **Training Time**: 15-20 minutes (fastest)
    - **Model Size**: ~4M parameters (smallest)
    - **Accuracy**: 98.48%
    - **Mobile-Ready**: Ideal for edge deployment
    
    **Best for:**
    - Real-time applications
    - Mobile/Edge devices
    - Resource-constrained environments
    """)

st.markdown("---")

# Load JSON report if available
if os.path.exists(report_json):
    with open(report_json, 'r') as f:
        report = json.load(f)
    
    st.markdown("### <i class='fa-solid fa-file-lines'></i> Detailed Report", unsafe_allow_html=True)
    
    with st.expander("View Full Report Data", expanded=False):
        st.json(report)

# Dataset information
st.markdown("---")
st.markdown("### <i class='fa-solid fa-database'></i> Dataset Information", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Images", "5,693")
with col2:
    st.metric("Training Set", "3,925 (68.9%)")
with col3:
    st.metric("Validation Set", "1,176 (20.6%)")
with col4:
    st.metric("Test Set", "1,176 (20.6%)")

st.info("""
**Dataset Characteristics:**
- Binary Classification: POTHOLE vs NOPOTHOLE
- Balanced Distribution: 50/50 split
- Image Resolution: 224×224 pixels (resized)
- Format: JPG, PNG
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 2rem 0;">
    <p style="margin: 0; font-size: 14px;">
        <i class="fa-solid fa-copyright"></i> 2024 Zeedan Mustami Argani | University of Muhammadiyah Malang
    </p>
    <p style="margin: 0.5rem 0 0 0; font-size: 12px; color: #666;">
        <i class="fa-solid fa-chart-bar"></i> Overall Dashboard - Model Performance Analysis
    </p>
</div>
""", unsafe_allow_html=True)