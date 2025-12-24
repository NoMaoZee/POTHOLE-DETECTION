"""
Script to re-save models in compatible format
This fixes the 'batch_shape' error by converting old model format to new format
"""

import os
import tensorflow as tf
from tensorflow import keras

# Model paths
models_to_fix = [
    ("PureCNN/Model/final_model.keras", "PureCNN/Model/final_model_fixed.keras"),
    ("ResNet50/Model/resnet50_final.keras", "ResNet50/Model/resnet50_final_fixed.keras"),
    ("EfficientNet/Model/efficientnet_final.keras", "EfficientNet/Model/efficientnet_final_fixed.keras"),
]

def fix_model(old_path, new_path):
    """Load and re-save model in compatible format"""
    print(f"\n{'='*60}")
    print(f"Processing: {old_path}")
    print(f"{'='*60}")
    
    if not os.path.exists(old_path):
        print(f"❌ Model not found: {old_path}")
        return False
    
    try:
        # Load model with compile=False to avoid optimizer issues
        print("Loading model...")
        model = keras.models.load_model(old_path, compile=False)
        print(f"✅ Model loaded successfully!")
        print(f"   Input shape: {model.input_shape}")
        print(f"   Output shape: {model.output_shape}")
        
        # Re-compile with simple optimizer
        print("Re-compiling model...")
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        # Save in new format
        print(f"Saving to: {new_path}")
        model.save(new_path, save_format='keras')
        print(f"✅ Model saved successfully!")
        
        # Verify the new model can be loaded
        print("Verifying new model...")
        test_model = keras.models.load_model(new_path)
        print(f"✅ Verification successful!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    print("\n" + "="*60)
    print("MODEL FORMAT FIXER")
    print("="*60)
    print("This script will re-save your models in a compatible format")
    print("to fix the 'batch_shape' error on Streamlit Cloud.\n")
    
    success_count = 0
    total_count = len(models_to_fix)
    
    for old_path, new_path in models_to_fix:
        if fix_model(old_path, new_path):
            success_count += 1
    
    print("\n" + "="*60)
    print(f"SUMMARY: {success_count}/{total_count} models fixed successfully")
    print("="*60)
    
    if success_count == total_count:
        print("\n✅ All models fixed!")
        print("\nNext steps:")
        print("1. Update model_loader.py to use the *_fixed.keras files")
        print("2. Commit and push to GitHub")
        print("3. Streamlit Cloud will automatically redeploy")
    else:
        print("\n⚠️ Some models failed to convert.")
        print("Please check the error messages above.")

if __name__ == "__main__":
    main()
