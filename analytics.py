
import streamlit as st
import requests
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

# Title of the application
st.title("HTTP Requests with Streamlit")

# GET request
st.header("GET Request")
response_get = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response_get.status_code == 200:
    st.write("GET request successful!")
    st.write("Response:")
    st.write(response_get.json())
else:
    st.write("GET request failed!")

# POST request
st.header("POST Request")
data = {
    "title": "Streamlit Request",
    "body": "This is a sample request",
    "userId": 1
}
response_post = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
if response_post.status_code == 201:
    st.write("POST request successful!")
    st.write("Response:")
    st.write(response_post.json())
else:
    st.write("POST request failed!")

