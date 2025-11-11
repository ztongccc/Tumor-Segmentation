# Tumor Segmentation (Project of DS4420)

## Overview
This project aims to develop basic automated tumor segmentation systems based on two approches, **Convolutional Neural Networks (CNNs)** and **Bayesian Modeling**. The goal is to accurately segment tumor regions from medical images (e.g., MRI scans).

## Dataset
The dataset for this project is found on Kaggle(https://www.kaggle.com/datasets/jakeshbohaju/brain-tumor?select=Brain+Tumor)
This is a brain tumor feature dataset including five first-order features and eight texture features with the target level (in the column Class).

* First Order Features
    * Mean
    * Variance
    * Standard Deviation
    * Skewness
    * Kurtosis

* Second Order Features
    * Contrast
    * Energy
    * ASM (Angular second moment)
    * Entropy
    * Homogeneity
    * Dissimilarity
    * Correlation
    * Coarseness

Image column defines image name and Class column defines either the image has tumor or not (1 = Tumor, 0 = Non-Tumor)

## Methodology
  - **CNN**

  - **Bayesian Model**