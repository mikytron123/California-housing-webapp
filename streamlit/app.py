import streamlit as st
import pandas as pd
import requests


def main():
    # headers
    st.title("California Housing Model")
    st.write("This app enables users to make predictions using a scikit learn model")
    # data upload
    st.subheader("1. Data upload")
    st.write("Upload a csv for predictions")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
    # prediction
    st.subheader("2. Predictions")
    if st.button("Get Predictions"):
        jsonreq = requests.post("http://api:3000/predict", json=df.to_dict())
        preds = jsonreq.json()
        df["Predictions"] = preds
        st.write(df)


if __name__ == "__main__":
    main()
