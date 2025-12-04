import streamlit as st

def main():
    st.set_page_config(
        page_title="Tumor Segmentation Project",
        page_icon="🧠",
        layout="wide"
    )

    st.title("🧠 Tumor Segmentation Project")
    st.markdown("### DS4420 Project")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Overview", "Dataset", "Methodology", "Team"])

    if options == "Overview":
        st.header("Project Overview")
        st.write("""
        This project aims to develop basic automated tumor segmentation systems based on two approaches:
        - **Convolutional Neural Networks (CNNs)**
        - **Bayesian Modeling**
        
        The goal is to accurately segment tumor regions from medical images (e.g., MRI scans).
        """)
        
        st.info("Automated segmentation can significantly aid radiologists in diagnosis and treatment planning.")

    elif options == "Dataset":
        st.header("Dataset Information")
        st.write("The dataset for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/jakeshbohaju/brain-tumor?select=Brain+Tumor).")
        
        st.markdown("""
        It includes a brain tumor feature dataset with:
        - **Five first-order features**
        - **Eight texture features**
        - **Target level** (Class: 1 = Tumor, 0 = Non-Tumor)
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("First Order Features")
            st.markdown("""
            - Mean
            - Variance
            - Standard Deviation
            - Skewness
            - Kurtosis
            """)
            
        with col2:
            st.subheader("Second Order Features")
            st.markdown("""
            - Contrast
            - Energy
            - ASM (Angular second moment)
            - Entropy
            - Homogeneity
            - Dissimilarity
            - Correlation
            - Coarseness
            """)

    elif options == "Methodology":
        st.header("Methodology")
        
        st.subheader("1. Convolutional Neural Networks (CNNs)")
        st.write("""
        We utilize CNNs for their powerful ability to learn spatial hierarchies of features automatically and adaptively from input images.
        (More details to be added as implementation progresses)
        """)
        
        st.divider()
        
        st.subheader("2. Bayesian Modeling")
        st.write("""
        We explore Bayesian approaches to incorporate uncertainty quantification in our segmentation predictions.
        (More details to be added as implementation progresses)
        """)

    elif options == "Team":
        st.header("Team")
        st.write("DS4420 Project Team")

if __name__ == "__main__":
    main()
