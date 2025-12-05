import streamlit as st
from pathlib import Path

# Get the images directory path
IMAGES_DIR = Path(__file__).parent.parent / "images"

st.title("BNN - Bayesian Neural Networks")

# Methodology Section
st.header("Methodology")

st.markdown("""
A CNN with Monte Carlo Dropout applied, allowing for the estimation of predictive uncertainty for tumor classification from image data.
""")

st.subheader("Model Architecture")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Base Architecture:**
    - Convolutional Neural Network (CNN)
    - Similar structure to standard CNN
    - Uses convolutional and pooling layers
    """)

with col2:
    st.info("""
    **Bayesian Component:**
    - Monte Carlo Dropout
    - Multiple forward passes with dropout
    - Uncertainty estimation from prediction variance
    """)

st.markdown("---")

# Monte Carlo Dropout Explanation
st.subheader("Monte Carlo Dropout")

st.markdown("""
Monte Carlo Dropout is a technique that enables uncertainty estimation in neural networks:

1. **During Training**: Dropout randomly deactivates neurons to prevent overfitting
2. **During Testing**: Keep dropout active and run multiple forward passes
3. **Uncertainty Estimation**: Variation in predictions across passes indicates model uncertainty
""")

st.info("""
**Key Advantage:**

This approach combines the power of deep learning (CNN feature extraction) with uncertainty quantification (Bayesian inference), providing both high accuracy and confidence estimates.
""")

st.markdown("---")

# Results Section
st.header("Results")

st.markdown("""
Finally we get our Bayesian Neural Networks model, we get the final average loss: 0.2109, then we plotted Standard Reliability Diagram and it shows the results are align with the diagonal, means this model is accurate on clear cases and cautious on ambiguous cases.
""")

# Metrics
st.subheader("Performance Metrics")

col3, col4 = st.columns(2)

with col3:
    st.metric("Final Average Loss", "0.2109")

with col4:
    st.metric("Calibration", "✓ Well-calibrated")

st.markdown("---")

# Standard Reliability Diagram
st.subheader("Standard Reliability Diagram")

st.image(str(IMAGES_DIR / "reliability_diagram.png"), caption="Standard Reliability Diagram", use_container_width=True)

st.success("""
**Standard Reliability Diagram**

The reliability diagram shows:
- **X-axis**: Mean Predicted Probability (Confidence)
- **Y-axis**: True Probability (% Correct)
- **Blue line**: Model's calibration curve
- **Gray diagonal**: Perfect calibration

**Interpretation:**
- Points align closely with the diagonal line
- Model is **accurate on clear cases** (high confidence predictions are usually correct)
- Model is **cautious on ambiguous cases** (low confidence when uncertain)
- Well-calibrated predictions make the model trustworthy for clinical use
""")

st.caption("The reliability diagram demonstrates excellent calibration, with predictions aligning with the diagonal reference line")

st.markdown("---")

# Detailed Analysis
st.subheader("Model Reliability Analysis")

st.info("""
**What makes BNN valuable for medical imaging:**

1. **Uncertainty Awareness**: The model knows when it's unsure, which is critical for medical diagnosis
2. **Calibrated Predictions**: Predicted probabilities reflect actual accuracy rates
3. **Risk Management**: High-uncertainty cases can be flagged for expert review
4. **Trustworthiness**: Well-calibrated models build confidence in clinical settings
""")

st.markdown("---")

# Summary
st.success("""
**Summary:**

The Bayesian Neural Network combines the representational power of CNNs with uncertainty quantification through Monte Carlo Dropout. With a final average loss of 0.2109 and excellent calibration (shown in the reliability diagram), this model is particularly valuable for medical applications where knowing the confidence of predictions is as important as the predictions themselves. The model is accurate on clear cases and appropriately cautious on ambiguous ones, making it a trustworthy tool for clinical decision support.
""")
