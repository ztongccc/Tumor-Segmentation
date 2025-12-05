import streamlit as st

home = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
datasets = st.Page("pages/dataset.py", title="Dataset", icon=":material/dataset:")
cnn = st.Page("pages/cnn.py", title="CNN")
unet = st.Page("pages/unet.py", title="UNet")
bayesian = st.Page("pages/bayesian.py", title="Bayesian ML")
bnn = st.Page("pages/bnn.py", title="BNN")

pg = st.navigation({
    "Home": [home],
    "Data": [datasets],
    "Models": [cnn, unet, bayesian, bnn],
    })

pg.run()