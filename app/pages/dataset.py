import streamlit as st

st.title("Dataset")

st.markdown("""
The dataset we used for brain tumor classification is from Kaggle, which contains over 
3000 MRI brain images, and all of them are labeled with 1 (with tumor) and 0 (without tumor). 
To train CNN on this dataset, we have done several preprocessing steps, which are first, 
we resize image to 64*64, then we convert the data to DataLoader.
""")

# Classification Dataset Section
st.header("Brain Tumor Classification Dataset")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Details")
    st.markdown("""
    - **Source**: Kaggle
    - **Size**: Over 3000 MRI brain images
    - **Labels**: 
        - 1 = With tumor
        - 0 = Without tumor
    """)

with col2:
    st.subheader("Preprocessing Steps")
    st.markdown("""
    1. **Label**: Split the non-labeled images into labeled with train & test datasets
    2. **Resize**: Images resized to 64×64 pixels
    3. **DataLoader**: Use DataLoader to load the data in batches, and be ready for training
    """)

st.markdown("---")

# Sample Images Section for Classification
st.subheader("Sample Images")
col3, col4 = st.columns(2)

with col3:
    st.image("images/with_tumor.jpg", caption="MRI image containing a brain tumor")

with col4:
    st.image("images/without_tumor.jpg", caption="MRI image without a brain tumor")

st.markdown("---")

# Segmentation Dataset Section
st.header("Tumor Segmentation Dataset")

st.markdown("""
The second dataset used for tumor segmentation is also from Kaggle. We cannot use the first dataset for U-Net segmentation because it only provides labels for classification instead of pixel-level masks. U-Net needs paired image–mask data, so we use a separate dataset that includes ground truth segmentation masks. Before we train the model, we first resize images to [255, 255], and we flip and rotate the all part of the images to get more samples because the this sample is size is relative small, and also this helps avoid overfitting.
""")

col5, col6 = st.columns(2)

with col5:
    st.subheader("Dataset Details")
    st.markdown("""
    - **Source**: Kaggle
    - **Type**: Paired image-mask data
    - **Purpose**: Pixel-level tumor segmentation
    """)

with col6:
    st.subheader("Preprocessing Steps")
    st.markdown("""
    1. **Resize**: Images resized to 255×255 pixels
    2. **Data Augmentation**: 
        - Flip images
        - Rotate images
    3. **Purpose**: Increase sample size and avoid overfitting
    """)

st.markdown("---")

# Sample Images Section for Segmentation
st.subheader("Sample Segmentation Data")
col7, col8 = st.columns(2)

with col7:
    st.image("images/mask.png", caption="Raw image with tumor section highlighted")

with col8:
    st.image("images/raw_image.png", caption="Tumor section mask from the raw image")

st.markdown("---")

# Summary Section
st.header("Summary")

st.info("""
**Key Differences Between Datasets:**

- **Classification Dataset**: Provides binary labels (tumor/no tumor) for entire images. Used for CNN-based classification.
- **Segmentation Dataset**: Provides pixel-level masks showing exact tumor locations. Required for U-Net architecture.
""")

st.success("""
Both datasets are essential for different aspects of the project:
- Classification helps identify whether a tumor exists
- Segmentation helps locate and outline the tumor precisely
""")
