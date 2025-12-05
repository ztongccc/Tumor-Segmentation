import streamlit as st

st.title(" Brain Tumor Classification & Segmentation")

st.markdown("---")

st.header("Motivation")

st.markdown("""
Brain cancer is now a severe health issue to all humans, and the manual recognition and segmentation is very time consuming and low-efficient. Therefore, we would like to build a system for doctors that can automatically do all those staff, so that doctors can focus on coming up with the best treatment methods to help patients recover more efficient.
""")

col1, col2 = st.columns(2)

with col1:
    st.image("images/brain_tumor.png", caption="Brain tumor effects on human", use_container_width=True)
    st.info("""
    **Brain tumor effects on human**
    
    Brain tumors can affect various cognitive and physical functions, making early detection critical.
    """)

with col2:
    st.image("images/tumor_stages.png", caption="Brain tumor stages", use_container_width=True)
    st.info("""
    **Brain tumor stages**
    
    Understanding tumor development process helps in determining appropriate treatment strategies.
    """)

st.markdown("---")

# Project Overview
st.header("Project Overview")

st.markdown("""
This project implements and compares multiple approaches for brain tumor detection and segmentation from MRI images:

- **Classification Models**: Determining whether a brain tumor is present (CNN, Bayesian LR, BNN)
- **Segmentation Models**: Identifying the exact location and boundaries of tumors (U-Net)
- **Uncertainty Quantification**: Providing confidence estimates for predictions (Bayesian LR, BNN)
""")

st.markdown("---")

# Why Bayesian Methods?
st.header("Why Bayesian Methods?")

st.info("""
In medical diagnosis, knowing the **confidence** of a prediction is still very important, what can it do:

**Uncertainty Quantification**: Know when the model is unsure  
**Risk Management**: Flag uncertain cases for expert review  
**Clinical Trust**: Good predictions build confidence  
**Better Decision Making**: Doctors can prioritize cases based on model confidence  
""")

st.markdown("---")

# Navigation Guide
st.header("Navigation Guide")

st.markdown("""
Explore different sections of this project:

- **Home**: Project introduction and overview (you are here)
- **Dataset**: Details about the datasets and preprocessing steps
- **CNN**: Convolutional Neural Network for classification
- **UNet**: U-Net architecture for tumor segmentation
- **Bayesian ML**: Bayesian Logistic Regression with uncertainty
- **BNN**: Bayesian Neural Network with calibrated predictions
""")

st.markdown("---")

# Project information part
st.header("About This Project")

st.markdown("""
This project demonstrates the application of both traditional deep learning and Bayesian methods to medical image analysis, specifically brain tumor detection and segmentation. By combining multiple approaches, we aim to provide both high accuracy and meaningful uncertainty estimates to support clinical decision-making.
""")

st.success("""
💡 **Get Started**: Use the navigation menu on the left to explore different models and their results!
""")

st.markdown("---")

# Conclusion part
st.header("Project Conclusion")

st.markdown("""
Our CNN achieved strong performance in MRI classification with 0.834 accu-
racy, and the U-Net model generated meaningful segmentation masks with
a Dice score of 0.7335, demonstrating its ability to capture tumor structure
even with limited data. The Bayesian Logistic Regression and Bayesian Neu-
ral Network models further improved interpretability by providing uncertainty
estimates. Therefore, these models form a system for tumor recognition and
segmentation, and this system can provide different models in different situ-
ation or purpose.
""")

st.markdown("---")

# Future Work
st.header("Future Work")

st.markdown("""
In the future, we would like to improve our U-Net model’s overall performance,
especially in tumor boundary recogition, and try to use different models on
recognition part. Here are several tasks we would like to:

- **Try to implement ResNet**, which is the most widely used model in tumor
recognition industry nowadays, for recognition part.
- **Optimization prediction boundary** of the U-Net model to make the it more clear.
- **Add more stages data** In this project, we only focus on LGG(low-grade Glioma, an early stage,
stage I and stage II, of brain cancer), we would like to perform U-Net on the
rest stages of brain tumor, if the dataset is available.
""")