import streamlit as st

st.title("Bayesian ML - Bayesian Logistic Regression")

# Methodology Section
st.header("Methodology")

st.markdown("""
Extract image features with EBImage and fit a Bayesian logistic regression model in order to classify tumor images with posterior predictive uncertainty.
""")

st.subheader("Model Pipeline")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Feature Extraction:**
    - Use EBImage library
    - Extract relevant image features
    - Feature preprocessing and normalization
    """)

with col2:
    st.info("""
    **Bayesian Modeling:**
    - Bayesian logistic regression
    - Posterior predictive uncertainty estimation
    - Probabilistic classification
    """)

st.markdown("---")

# Key Concepts
st.subheader("Why Bayesian Approach?")

st.markdown("""
Unlike traditional point estimate models, Bayesian methods provide:
- **Uncertainty quantification**: Know how confident the model is in its predictions
- **Posterior distributions**: Full probability distributions over parameters
- **Interpretability**: Understand prediction confidence for clinical decision-making
""")

st.markdown("---")

# Results Section
st.header("Results")

st.markdown("""
For our Bayesian Logistic Regression model, we get 0.7703 as the test accuracy, and the model also converges after training.
""")

# Metrics
st.subheader("Performance Metrics")

col3, col4 = st.columns(2)

with col3:
    st.metric("Test Accuracy", "0.7703 (77.03%)")

with col4:
    st.metric("Model Convergence", "✓ Converged")

st.markdown("---")

# Model Characteristics
st.subheader("Model Characteristics")

st.info("""
**Key Findings:**

1. **Good Accuracy**: Achieved 77.03% test accuracy using Bayesian inference
2. **Successful Convergence**: Model converged properly during training, indicating stable parameter estimation
3. **Uncertainty Quantification**: Provides posterior predictive distributions for each classification
4. **Feature-based Approach**: Uses extracted image features rather than raw pixels
""")

st.markdown("---")

# Comparison
st.subheader("Comparison with CNN")

col5, col6 = st.columns(2)

with col5:
    st.warning("""
    **Bayesian Logistic Regression**
    - Accuracy: 77.03%
    - Provides uncertainty estimates
    - Feature-based approach
    - Faster training
    - More interpretable
    """)

with col6:
    st.success("""
    **CNN**
    - Accuracy: 83.40%
    - No uncertainty quantification
    - End-to-end learning
    - Longer training time
    - Less interpretable
    """)

st.markdown("---")

# Summary
st.success("""
**Summary:**

The Bayesian Logistic Regression model achieved 77.03% test accuracy with successful convergence. While slightly lower than the CNN's accuracy, this approach provides valuable uncertainty quantification, which is crucial for medical diagnosis where knowing the confidence of predictions can inform clinical decision-making.
""")
