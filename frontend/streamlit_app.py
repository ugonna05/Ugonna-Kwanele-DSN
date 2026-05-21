import streamlit as st
import requests


st.title("PersonaMind-AI")

query = st.text_input(
    "What kind of product are you looking for?"
)

if st.button("Get Recommendations"):

    response = requests.post(
        "http://127.0.0.1:8000/recommend",
        json={
            "user_id": "User_001",
            "query": query,
            "top_k": 5
        }
    )

    data = response.json()

    st.subheader("AI Reasoning")
    st.write(data['reasoning'])

    st.subheader("Recommendations")

    for rec in data['recommendations']:
        st.write(rec)