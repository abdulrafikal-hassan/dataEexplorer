import streamlit as st 
# importing pandas and numpy for working with a sample data
# to demonstrate streamlit

import numpy as np 
import pandas as pd
import time

st.title('My first app')
st.write("Here is our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
}))

"""
# My First App Ml webApp
Here is our 2nd attempt at using data to create a table:
"""

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

df

st.write("Creating a line chart using st.lin_chart()")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns =['a','b','c']
)

st.line_chart(chart_data)

st.write("Displaying data points on a map using st.map()")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(map_data)

st.write("Adding interactivity with Widges")

""" Using Checkbox to show/Hide data"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a','b','c']
    )

    st.line_chart(chart_data)

st.write("Using the Selectbox for options")

option1 = st.selectbox(
    'Which number do you like best? ',
    df['second column']
)

'You selected: ', option1

st.write("Putting Widgets in a sidebar")

option = st.sidebar.selectbox(
    'Which number do you like best? ',
    df['first column']
)

'You selected: ', option

"""Show Progress"""

'Starting a long computation......'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

    '....and now we are done!'