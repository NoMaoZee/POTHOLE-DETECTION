"""
Utils package for Pothole Detection Dashboard
"""

from .model_loader import (
    load_purecnn_model,
    load_resnet_model,
    load_efficientnet_model,
    get_model_info,
    check_model_exists,
    CLASS_NAMES
)

from .inference import (
    predict_image,
    compute_image_stats,
    generate_interpretation
)

from .gradcam import (
    predict_with_gradcam,
    make_gradcam_heatmap,
    generate_gradcam_overlay
)

from .styling import (
    get_base_css,
    get_purecnn_theme,
    get_resnet_theme,
    get_efficientnet_theme,
    get_home_theme
)

__all__ = [
    'load_purecnn_model',
    'load_resnet_model',
    'load_efficientnet_model',
    'get_model_info',
    'check_model_exists',
    'CLASS_NAMES',
    'predict_image',
    'compute_image_stats',
    'generate_interpretation',
    'predict_with_gradcam',
    'make_gradcam_heatmap',
    'generate_gradcam_overlay',
    'get_base_css',
    'get_purecnn_theme',
    'get_resnet_theme',
    'get_efficientnet_theme',
    'get_home_theme'
]