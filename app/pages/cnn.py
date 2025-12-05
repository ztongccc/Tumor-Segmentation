import streamlit as st
from pathlib import Path

# Get the images directory path
IMAGES_DIR = Path(__file__).parent.parent / "images"

st.title("CNN")

# Methodology Section
st.header("Methodology")

st.markdown("""
Using PyTorch library to construct convolution blocks with convolution layers, ReLU activation functions and Max-pooling layer, then terminating in a flattened fully connected layer that outputs logits for sigmoid-based prediction.
""")

st.subheader("Architecture Details")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Convolutional Blocks:**
    - Convolution layers
    - ReLU activation functions
    - Max-pooling layers
    """)

with col2:
    st.info("""
    **Output Layer:**
    - Flattened fully connected layer
    - Sigmoid-based prediction
    - Binary classification (tumor/no tumor)
    """)

st.markdown("---")

# Results Section
st.header("Results")

st.markdown("""
We used CNN to do the MRI classification, and got pretty good results.
""")

# Metrics
st.subheader("Performance Metrics")
col3, col4 = st.columns(2)

with col3:
    st.metric("Test Loss", "0.4565")

with col4:
    st.metric("Test Accuracy", "0.8340 (83.4%)")

st.markdown("---")

# Confusion Matrix Section
st.subheader("Confusion Matrix")

st.markdown("""
The confusion matrix below shows the classification performance on the test set:
""")

st.image(str(IMAGES_DIR / "cnn_confusion_matrix.png"), caption="Confusion Matrix of CNN", use_container_width=True)

st.info("""
**Confusion Matrix of CNN**

The confusion matrix demonstrates strong performance in both classes:
- High true positive rate for tumor detection
- High true negative rate for non-tumor images
- Low false positive and false negative rates
""")

st.markdown("---")

# Summary
st.success("""
**Summary:**

The CNN model achieved excellent results with 83.4% accuracy on the test set. The model successfully learned to distinguish between brain MRI images with and without tumors using convolutional feature extraction and sigmoid-based classification.
""")
