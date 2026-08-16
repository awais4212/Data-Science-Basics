import streamlit as st
import pandas as pd
import numpy as np

#heading
st.title('Welcome To my page')

#simple Text
st.write('This is the simple Text')

# DataFrame
df = pd.DataFrame({
    'Data': [1,2,3,34,2],
    'Data1': [11,21,31,34,21]
    }
)
st.write(df)

#Create a Line Chart
chartdata = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chartdata)