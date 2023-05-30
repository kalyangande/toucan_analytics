import streamlit as st
import matplotlib.pyplot as plt
import requests
import json
import streamlit as st
from django.http import request
import streamlit as st
import pandas as pd
import altair as alt


import streamlit as st

    
col1, col2 = st.columns(2, gap="large")

with col1:
    st.header("PIE Chart")
    #  User input form
    url = "http://127.0.0.1:8000/analytics/?type=pie"
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()
        labels = data['labels']
        sizes = data['sizes']
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    
        explode = [0,0,0,0,0,0]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
        st.write('\n')
    else:
        st.error(f'Error: {response.status_code}')
        

with col2:
    st.header("Mode of Payments per Year")
    get_method=requests.get('http://127.0.0.1:8000/analytics/?type=bar')
    if get_method.status_code == 200:
        # Extract the data from the response
        data = get_method.json()
        mode_list = data['mode']
        amount_list = data['amount']
        source = pd.DataFrame({
            'Amount_spent': amount_list,
            'Mode of Payment': mode_list
        })
        bar_chart = alt.Chart(source).mark_bar().encode(
            y='Amount_spent:Q',
            x='Mode of Payment:O',
        )
        st.altair_chart(bar_chart, use_container_width=True)
        st.write('\n')
    else:
        st.error(f'Error: {get_method.status_code}')


col3, col4 = st.columns(2)
with col3:
    st.header("Mode of Payments per Year")
    get_method=requests.get('http://127.0.0.1:8000/analytics/?type=emi')
    if get_method.status_code == 200:
        # Extract the data from the response
        data = get_method.json()
        in_time = data['in_time']
        total = data['total']
        source = pd.DataFrame({
            'EMI PAID ON TIME': in_time,
            'NUMBER OF CUSTOMERS': total
        })
        bar_chart = alt.Chart(source).mark_bar().encode(
            x='EMI PAID ON TIME:O',
            y='NUMBER OF CUSTOMERS:Q',
        )
        st.altair_chart(bar_chart, use_container_width=True)
        st.write('\n')
    else:
        st.error(f'Error: {get_method.status_code}')

with col4:
    st.header("Frequent Mode Transanction by an individual Customer")
    get_method=requests.get('http://127.0.0.1:8000/analytics/?type=table')
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
        st.dataframe(df)
        # # Add a serial number column
        # df.insert(0, 'S.No', range(1, len(df) + 1))
        # # Convert DataFrame to HTML table without index column
        # html_table = df.to_html(index=False)
        # # Display the table
        # st.write(html_table, unsafe_allow_html=True)
        # st.write('\n')
    else:
        st.error(f'Error: {get_method.status_code}')
    



   
    
