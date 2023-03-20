import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import altair as alt
from vega_datasets import data
st.subheader("Competitors Analysis")

df2 = pd.read_csv('competitora.csv')
st.write("<span style=\"font-size:20px;\">Zipcode 90012's restaurants has higher average rating and number of reviews on Yelp</span>", unsafe_allow_html=True)

#df3=pd.Dataframes()
def avg(zipcode,name,df):
    df_test=df[df['zipcode'] ==int(zipcode)]
    number = df_test[name].mean()
    formatted_num = "{:.2f}".format(number)
    return formatted_num
data = {'zipcode': ['90012', '90013', '90007'],
        'average rate': [avg('90012','rate',df2), avg('90013','rate',df2), avg('90007','rate',df2)],
        'Average reviews': [avg('90012','reviews',df2), avg('90013','reviews',df2), avg('90007','reviews',df2)]}
df4 = pd.DataFrame(data)
st.dataframe(df4)

input1='datasets_clean.csv'

df = pd.read_csv(input1)
st.subheader('Correlation')
st.write('<style>body {font-family: Arial, sans-serif;}</style>', unsafe_allow_html=True)
st.write('<span style="font-size:20px;">House value and household income has a positive correlation relationship.</span>', unsafe_allow_html=True)

# st.write('<span style="font-size:20px; color:blue">House value and household income has a positive correlation relationship.</span>', unsafe_allow_html=True)



sns.pairplot(df[['Population', 'income', 'house value']])
st.pyplot()

