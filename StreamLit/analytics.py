# Login -> jwt token save
# subsequent calls get – header – put jwt token and issue get calls

import streamlit as st
import matplotlib.pyplot as plt
import requests
import json
import streamlit as st
from django.http import request
import streamlit as st
import pandas as pd
import altair as alt
import datetime

st.set_page_config(layout="wide")

local_host = 'http://52.90.18.143:8000/'


# Create a session state object
session_state = st.session_state

def get_jwt_token(username, password):
    url = local_host + 'api/token/'
    data = {
        'username': username,
        'password': password
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        token = response.json()
        access_token = token['access']
        return access_token
    else:
        return None
    

def get_data(token):
    url = local_host + 'data/'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_data_for_analytics_views(token):
    url = local_host + 'analytics/'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
token = " "   
def login_page():
    st.markdown("<h1 style='text-align: center; '>Login Page</h1> <br>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        col1, col2,col3,col4,col5 = st.columns(5)
        with col3:
            login_button = st.button("Login")

    if login_button:
        token = get_jwt_token(username, password)
        if token:
            # st.success('Authentication successful!')
            # st.write('JWT Token:', token)
            data = get_data(token)
            st.write(data)
            data = get_data_for_analytics_views(token)
            st.write(data)
            if data:
                return True  

        else:
            st.error("Invalid username or password.")
            return False  # Return False to indicate unsuccessful login
        
# login_success = login_page()

# Display the login page
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    login_success = login_page()

    if login_success:
        st.session_state['logged_in'] = True
        st.experimental_rerun()
else:
    
    st.markdown("<h1 style='text-align: center; '>Toucan Analytics</h1> <br>", unsafe_allow_html=True)

    # "2023-01-01", "2023-12-31"

    min_date = datetime.date(2023, 1, 1)
    max_date = datetime.date(2023, 12, 31)

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        st.write("")
    with col2:
        st.write("")
    with col3:
        st.write("")
    with col4:
        st.write("")
    with col5:
        st.write("")
    with col6:
        st.write("")
    with col7:
        start_date = st.date_input("Start Date", min_value=min_date, max_value=max_date,value=min_date)
    with col8:
        end_date = st.date_input("End Date", min_value=min_date, max_value=max_date,value=max_date)


    if start_date and end_date:
        if start_date > end_date:
            st.error("Error: Start Date must be before End Date.")
        else:
            params = {
            "start_date": str(start_date),
            "end_date": str(end_date)
        }
        
# table_url = "http://127.0.0.1:8000/analytics/?type=table&start_date={start_date_str}&end_date={end_date_str}"



    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("<h2 style='text-align: center;margin-bottom:10px'>PIE CHART</h2>", unsafe_allow_html=True)
        url = local_host + 'analytics/?type=pie'
        get_data_for_analytics_views(token)
        response = requests.get(url,params=params)
        if response.status_code == 200:
            # Extract the data from the response
            data = response.json()
            labels = data['labels']
            sizes = data['sizes']
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            colors = ['violet','indigo','blue','green','yellow','orange']
            wedgeprops = {'linewidth': 0.5, 'edgecolor': 'white'}
            explode = [0,0,0,0,0,0]
            fig1, ax1 = plt.subplots(figsize=(4, 4))
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90,colors=colors,wedgeprops=wedgeprops)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)
            st.write('\n')
        else:
            st.error(f'Error: {response.status_code}')
            

    with col2:
    
        st.markdown("<h2 style='text-align: center;'>Amount Spent Vs Mode of Payments</h2>", unsafe_allow_html=True)
        st.header("\n")
        url = local_host + 'analytics/?type=bar'
        get_data_for_analytics_views(token)
        get_method=requests.get(url,params=params)
        if get_method.status_code == 200:
            # Extract the data from the response
            data = get_method.json()
            mode_list = data['mode']
            amount_list = data['amount']
            source = pd.DataFrame({
                'Amount Spent': amount_list,
                'Mode of Payment': mode_list
            })
            bar_chart = alt.Chart(source).mark_bar(size=50).encode(
                y='Amount Spent:Q',
                x='Mode of Payment:O',
            )
            st.altair_chart(bar_chart, use_container_width=True)
            st.write('\n')
        else:
            st.error(f'Error: {get_method.status_code}')


    col3, col4 = st.columns(2, gap="large")
    with col3:
        st.markdown("<h2 style='text-align: center;margin-bottom:20px'>EMI RE-PAYMENTS</h2>", unsafe_allow_html=True)
        get_data_for_analytics_views(token)
        url = local_host + 'analytics/?type=emi'
        get_method=requests.get(url)
        if get_method.status_code == 200:
            # Extract the data from the response
            data = get_method.json()
            in_time = data['in_time']
            total = data['total']
            source = pd.DataFrame({
                'EMI PAID ON TIME': in_time,
                'NUMBER OF CUSTOMERS': total
            })
            bar_chart = alt.Chart(source).mark_bar(size=70).encode(
                x='EMI PAID ON TIME:O',
                y='NUMBER OF CUSTOMERS:Q',
            )
            st.altair_chart(bar_chart, use_container_width=True)
            st.write('\n')
        else:
            st.error(f'Error: {get_method.status_code}')

    with col4:
        st.markdown("<h2 style='text-align: center;margin-bottom:20px'>Frequent Mode Transanction of by an individual Customer</h2>", unsafe_allow_html=True)
        get_data_for_analytics_views(token)
        url = local_host + 'analytics/?type=table'
        get_method=requests.get(url,params=params)
        if get_method.status_code == 200:
            # Extract the data from the response
            data = get_method.json()
            customer = data['customer']
            mode = data['values']
            
        # Create a sample data frame
            data = {
                'Customer Id': [i for i in customer],
                'Frequent mode of Transanction': [i for i in mode],
            }
            df = pd.DataFrame(data)

            # Insert the 'S.No' column
            # df.insert(0, 'S.No', range(1, len(df) + 1))


            st.dataframe(df, height=350)
            
        else:
            st.error(f'Error: {get_method.status_code}')
        
