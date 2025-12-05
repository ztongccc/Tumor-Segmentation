import streamlit as st

st.title("U-Net - Tumor Segmentation")

# Methodology Section
st.header("Methodology")

st.markdown("""
Preprocessing MRI images with geometric and intensity augmentations, pair them with tumor masks, and train a U-Net segmentation model optimized with a combined BCE–Dice loss to learn accurate tumor region predictions.
""")

st.subheader("Model Pipeline")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Preprocessing:**
    - Geometric augmentations (rotation, flipping)
    - Intensity augmentations
    - Image-mask pairing
    - Image resize to 255×255
    """)

with col2:
    st.info("""
    **U-Net Architecture:**
    - Encoder-decoder structure
    - Skip connections
    - Combined BCE-Dice loss function
    - Pixel-level tumor prediction
    """)

st.markdown("---")

# Results Section
st.header("Results")

st.markdown("""
After that, we use UNet to do the tumor segmentation, the results are:
""")

# Metrics
st.subheader("Performance Metrics")

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Train Loss", "0.1648")

with col4:
    st.metric("Train Dice Coefficient", "0.6922")

with col5:
    st.metric("", "")

col6, col7, col8 = st.columns(3)

with col6:
    st.metric("Validation Loss", "0.1413")

with col7:
    st.metric("Val Dice Coefficient", "0.7335")

with col8:
    st.metric("", "")

st.markdown("---")

# Segmentation Results
st.subheader("Segmentation Examples")

st.success("""
**Fig. 7: Demonstration of UNet result**

The visualization shows three columns:
1. **Original MRI Image**: Raw brain scan with tumor
2. **Ground Truth Mask**: Expert-labeled tumor region
3. **Predicted Mask**: Model's predicted tumor segmentation

The model successfully identifies and segments tumor regions with high accuracy.
""")

st.caption("Sample segmentation results would be displayed here showing input images, ground truth masks, and predicted masks")

st.markdown("---")

# Performance Analysis
st.subheader("Model Performance Analysis")

st.info("""
**Dice Coefficient Interpretation:**
- Score of 0.7335 on validation set indicates strong overlap between predicted and ground truth masks
- Low validation loss (0.1413) suggests good generalization
- Combined BCE-Dice loss helps balance pixel-wise accuracy and region overlap
""")

st.markdown("---")

# Summary
st.success("""
**Summary:**

The U-Net model achieved strong segmentation performance with a Dice coefficient of 0.7335 on the validation set. The combined BCE-Dice loss function helps the model learn accurate pixel-level predictions for tumor regions, making it suitable for medical image segmentation tasks.
""")
