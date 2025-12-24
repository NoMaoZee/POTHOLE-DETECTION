"""
Styling utilities for Streamlit dashboard
Provides theme-based CSS for each model
"""

def get_base_css():
    """Base CSS for all pages"""
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

        * {
            font-family: 'Inter', sans-serif;
        }

        .main {
            background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
        }

        h1, h2, h3, h4 {
            color: #ffffff;
            font-weight: 600;
        }

        .stButton>button {
            border-radius: 10px;
            padding: 0.7rem 2.5rem;
            font-weight: 600;
            font-size: 16px;
            border: none;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        [data-testid="stMetricValue"] {
            font-size: 32px;
            font-weight: 700;
        }

        [data-testid="stMetricLabel"] {
            color: #b8b8b8 !important;
            font-weight: 500;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        [data-testid="metric-container"] {
            border-radius: 12px;
            padding: 1.2rem;
            transition: all 0.3s ease;
        }

        [data-testid="metric-container"]:hover {
            transform: translateY(-5px);
        }

        [data-testid="stFileUploader"] {
            border-radius: 12px;
            padding: 2rem;
        }

        .stTabs [data-baseweb="tab-list"] {
            border-radius: 10px;
            padding: 0.5rem;
            gap: 10px;
        }

        .stTabs [data-baseweb="tab"] {
            background: transparent;
            color: #b8b8b8;
            border-radius: 8px;
            padding: 0.8rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        hr {
            border: none;
            height: 2px;
            margin: 2rem 0;
        }

        footer {
            color: #888;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }
    </style>
    """

def get_purecnn_theme():
    """Blue + Black theme for PureCNN"""
    return """
    <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #001a33 0%, #003366 50%, #000000 100%);
            border-right: 2px solid #1976D2;
        }

        h1 {
            background: linear-gradient(90deg, #1976D2 0%, #42A5F5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2 {
            color: #42A5F5;
            border-bottom: 2px solid #1976D2;
            padding-bottom: 0.5rem;
        }

        [data-testid="stMetricValue"] {
            background: linear-gradient(90deg, #1976D2 0%, #42A5F5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        [data-testid="metric-container"] {
            background: rgba(25, 118, 210, 0.1);
            border: 1px solid #1976D2;
            box-shadow: 0 4px 15px rgba(25, 118, 210, 0.2);
        }

        [data-testid="metric-container"]:hover {
            box-shadow: 0 8px 25px rgba(25, 118, 210, 0.4);
            border-color: #42A5F5;
        }

        .stButton>button {
            background: linear-gradient(135deg, #1976D2 0%, #42A5F5 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(25, 118, 210, 0.3);
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #42A5F5 0%, #64B5F6 100%);
            box-shadow: 0 6px 20px rgba(25, 118, 210, 0.5);
        }

        [data-testid="stFileUploader"] {
            background: rgba(25, 118, 210, 0.05);
            border: 2px dashed #1976D2;
        }

        .stTabs [data-baseweb="tab-list"] {
            background: rgba(0, 26, 51, 0.8);
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #1976D2 0%, #42A5F5 100%);
            color: white !important;
        }

        .stAlert {
            border-left: 4px solid #1976D2;
            background: rgba(25, 118, 210, 0.1);
        }

        hr {
            background: linear-gradient(90deg, transparent 0%, #1976D2 50%, transparent 100%);
        }

        footer {
            border-top: 1px solid #1976D2;
        }
    </style>
    """

def get_resnet_theme():
    """Purple + Black theme for ResNet50"""
    return """
    <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a0033 0%, #2d0052 50%, #000000 100%);
            border-right: 2px solid #7B1FA2;
        }

        h1 {
            background: linear-gradient(90deg, #7B1FA2 0%, #AB47BC 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2 {
            color: #AB47BC;
            border-bottom: 2px solid #7B1FA2;
            padding-bottom: 0.5rem;
        }

        [data-testid="stMetricValue"] {
            background: linear-gradient(90deg, #7B1FA2 0%, #AB47BC 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        [data-testid="metric-container"] {
            background: rgba(123, 31, 162, 0.1);
            border: 1px solid #7B1FA2;
            box-shadow: 0 4px 15px rgba(123, 31, 162, 0.2);
        }

        [data-testid="metric-container"]:hover {
            box-shadow: 0 8px 25px rgba(123, 31, 162, 0.4);
            border-color: #AB47BC;
        }

        .stButton>button {
            background: linear-gradient(135deg, #7B1FA2 0%, #AB47BC 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(123, 31, 162, 0.3);
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #AB47BC 0%, #CE93D8 100%);
            box-shadow: 0 6px 20px rgba(123, 31, 162, 0.5);
        }

        [data-testid="stFileUploader"] {
            background: rgba(123, 31, 162, 0.05);
            border: 2px dashed #7B1FA2;
        }

        .stTabs [data-baseweb="tab-list"] {
            background: rgba(26, 0, 51, 0.8);
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #7B1FA2 0%, #AB47BC 100%);
            color: white !important;
        }

        .stAlert {
            border-left: 4px solid #7B1FA2;
            background: rgba(123, 31, 162, 0.1);
        }

        hr {
            background: linear-gradient(90deg, transparent 0%, #7B1FA2 50%, transparent 100%);
        }

        footer {
            border-top: 1px solid #7B1FA2;
        }
    </style>
    """

def get_efficientnet_theme():
    """Orange + Black theme for EfficientNet"""
    return """
    <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #331400 0%, #662900 50%, #000000 100%);
            border-right: 2px solid #E65100;
        }

        h1 {
            background: linear-gradient(90deg, #E65100 0%, #FF6F00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2 {
            color: #FF6F00;
            border-bottom: 2px solid #E65100;
            padding-bottom: 0.5rem;
        }

        [data-testid="stMetricValue"] {
            background: linear-gradient(90deg, #E65100 0%, #FF6F00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        [data-testid="metric-container"] {
            background: rgba(230, 81, 0, 0.1);
            border: 1px solid #E65100;
            box-shadow: 0 4px 15px rgba(230, 81, 0, 0.2);
        }

        [data-testid="metric-container"]:hover {
            box-shadow: 0 8px 25px rgba(230, 81, 0, 0.4);
            border-color: #FF6F00;
        }

        .stButton>button {
            background: linear-gradient(135deg, #E65100 0%, #FF6F00 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(230, 81, 0, 0.3);
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #FF6F00 0%, #FF8F00 100%);
            box-shadow: 0 6px 20px rgba(230, 81, 0, 0.5);
        }

        [data-testid="stFileUploader"] {
            background: rgba(230, 81, 0, 0.05);
            border: 2px dashed #E65100;
        }

        .stTabs [data-baseweb="tab-list"] {
            background: rgba(51, 20, 0, 0.8);
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #E65100 0%, #FF6F00 100%);
            color: white !important;
        }

        .stAlert {
            border-left: 4px solid #E65100;
            background: rgba(230, 81, 0, 0.1);
        }

        hr {
            background: linear-gradient(90deg, transparent 0%, #E65100 50%, transparent 100%);
        }

        footer {
            border-top: 1px solid #E65100;
        }
    </style>
    """

def get_home_theme():
    """Neutral theme for home/dashboard"""
    return """
    <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f0f0f 100%);
            border-right: 2px solid #4a4a4a;
        }

        h1 {
            background: linear-gradient(90deg, #ffffff 0%, #cccccc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2 {
            color: #ffffff;
            border-bottom: 2px solid #4a4a4a;
            padding-bottom: 0.5rem;
        }

        [data-testid="stMetricValue"] {
            background: linear-gradient(90deg, #ffffff 0%, #cccccc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        [data-testid="metric-container"] {
            background: rgba(74, 74, 74, 0.1);
            border: 1px solid #4a4a4a;
            box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
        }

        [data-testid="metric-container"]:hover {
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.2);
            border-color: #6a6a6a;
        }

        .stButton>button {
            background: linear-gradient(135deg, #4a4a4a 0%, #6a6a6a 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(74, 74, 74, 0.3);
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #6a6a6a 0%, #8a8a8a 100%);
            box-shadow: 0 6px 20px rgba(74, 74, 74, 0.5);
        }

        hr {
            background: linear-gradient(90deg, transparent 0%, #4a4a4a 50%, transparent 100%);
        }

        footer {
            border-top: 1px solid #4a4a4a;
        }
    </style>
    """