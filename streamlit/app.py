import streamlit as st
import pandas as pd
import requests
import os

API_PORT = str(os.getenv("API_PORT"))
API_HOST = str(os.getenv("API_HOST",default="localhost"))


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
        st.dataframe(
            df.head(),
            column_config={
                "_index": None,
            },
        )
    # prediction
    st.subheader("2. Predictions")
    if st.button("Get Predictions"):
        jsonreq = requests.post(
            f"http://{API_HOST}:{API_PORT}/predict", json={"input_data": df.to_dict(orient="records")}
        )
        preds = jsonreq.json()
        df["Predictions"] = preds
        st.dataframe(
            df,
            column_config={
                "_index": None,
            },
        )


if __name__ == "__main__":
    main()
