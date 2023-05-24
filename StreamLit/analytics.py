import streamlit as st
import matplotlib.pyplot as plt
import requests
import json
import streamlit as st
from django.http import request
import streamlit as st

col1, col2= st.columns(2)

data = {
            "title": "Streamlit Request",
            "body": "This is a sample request",
            "userId": 1
        }
with col1:
    if st.button('Post'):
        response_post = requests.post("http://127.0.0.1:8000/analytics", data=data)
        if response_post.status_code == 200:
            st.write("POST request successful!")
            st.write(data)
        else:
            st.write(f"POST request failed! {response_post.status_code}")
    else:
        st.write('click here')

with col2:
    a=st.button
    if a('get'):
        response_get = requests.get("http://127.0.0.1:8000/analytics")
        if response_get.status_code == 200:
            st.write("GET request successful!")
            st.write("Response:")
            st.write(response_get.json())
            
            
        else:
            st.write(f"GET request failed! {response_get.status_code}")
    else:
        st.write('click here')






