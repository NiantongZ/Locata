import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import matplotlib.pyplot as plt
import plotly.graph_objs as go
st.set_option('deprecation.showPyplotGlobalUse', False)


def avg(zipcode,name,df):
    df2=df[df['ZIP CODE'] == int(zipcode)]
    number = int(df2[name].mean())
    if name=='Population':
        formatted_number = '{:,.0f}'.format(number)
    else:
        formatted_number = '${:,.0f}'.format(number)
    return formatted_number
def difference(zip,df,name):
    df2 = df[df['ZIP CODE'].isin([90012, 90007,90013])]
    average=int(df2[name].mean())
    t=df2[df2['ZIP CODE']==int(zip)]
    number=int(t[name].mean())/int(average)
    formatted_number = '{:,.0f}%'.format(int(number))
    return formatted_number
def sum(zip,df,name):
    df2 = df[df['ZIP CODE'].isin([90012, 90007, 90013])]
    df3=df2[df2['ZIP CODE'] == int(zip)]
    total=len(df2[name])
    partial=len(df3[name])
    return [partial,int(partial/total)]

def plot_pie(zip_code, business_type, df):
    zip_code_df = df[df['ZIP CODE'] == zip_code]
    top_types = zip_code_df['PRIMARY NAICS DESCRIPTION'].value_counts().nlargest(8).index

    # replace all other types with "Others"
    zip_code_df['PRIMARY NAICS DESCRIPTION'] = zip_code_df['PRIMARY NAICS DESCRIPTION'].apply(
        lambda x: x if x in top_types else 'Others')

    # group the filtered DataFrame by "Business Type" and calculate the counts
    grouped = zip_code_df.groupby('PRIMARY NAICS DESCRIPTION').size()

    # calculate the percentage of the specific business type compared to all business types
    percentage = grouped[business_type] / grouped.sum() * 100

    labels = grouped.index
    sizes = grouped.values
    colors = ['lightblue', 'pink', 'lightgreen']
    explode = [0.1 if label == business_type else 0 for label in labels]
    plt.figure(figsize=(20, 20))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
        # add a title and display the pie chart
    plt.title(f"Percentage of {business_type}s in {zip_code}")
    plt.axis('equal')

    st.pyplot()

def plot_line(zip_code,business_type,df):
    df_filtered = df[(df['ZIP CODE'] == zip_code) & (df['PRIMARY NAICS DESCRIPTION'].str.contains(business_type, case=False))]
    df_filtered['LOCATION START YEAR'] = pd.to_datetime(df['LOCATION START DATE'], format="%m/%d/%y").dt.year
    print(df_filtered)
    year_counts = df_filtered['LOCATION START YEAR'].value_counts().sort_index()
    x = year_counts.index
    y = year_counts.values
    p = figure(
        title='Number of Business Started',
        x_axis_label='Location Start Year',
        y_axis_label='Count')

    p.line(x, y, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)



def zipcode(zip,df):
    st.subheader("Zipcode Dashboard,"+zip)
    col1, col2, col3,col4 = st.columns(4)
    col1.metric("House Value", avg(zip,"house value",df), difference(zip, df, 'house value'))
    col2.metric("Income", avg(zip,"income",df), difference(zip, df, 'income'))
    sum1=sum(zip, df, 'income')
    col3.metric("Competitors", sum1[0], sum1[1])
    col4.metric("Population", avg(zip,"Population",df), difference(zip, df, 'Population'))
    st.caption('This is a string that explains something above.')
    # plot graph
    plot_pie(int(zip), 'Full-service restaurants', df)
    # map density for each zipcode
    # df2=df[['lat', 'lon']] [(df['PRIMARY NAICS DESCRIPTION'] == 'Full-service restaurants') & (df['ZIP CODE'] == 90012)]
    df2 = df[['lat', 'lon']][(df['PRIMARY NAICS DESCRIPTION'] == 'Full-service restaurants')&(df['ZIP CODE'] == int(zip))]
    st.map(df2)
    st.caption('This is a string that explains map plot.')
    # plot line graph
    plot_line(int(zip), 'Full-service restaurants', df)
def compare():
    st.subheader("Zipcode Compare")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("90012")
        st.markdown(":green[House value ] "+ avg('90012',"house value",df))
        st.markdown(":orange[House value ] " + avg('90012',"income",df))
        sum1 = sum('90012', df, 'income')
        st.markdown(":violet[Competitor ] " + str(sum1[0]))
        st.markdown(":blue[Population ] " + avg('90012',"Population",df))

    with col2:
        st.subheader("90013")
        st.markdown(":green[House value] "+ avg('90013',"house value",df))
        st.markdown(":orange[House value] " + avg('90013',"income",df))
        sum2 = sum('90013', df, 'income')
        st.markdown(":violet[Competitor] " + str(sum2[0]))
        st.markdown(":blue[Population] " + avg('90013',"Population",df))
    with col3:
        st.subheader("90007")
        st.markdown(":green[House value] " + avg('90007',"house value",df))
        st.markdown(":orange[House value] " + avg('90007',"income",df))
        sum3 = sum('90007', df, 'income')
        st.markdown(":violet[Competitor] " + str(sum3[0]))
        st.markdown(":blue[Population] " + avg('90007',"Population",df))

input1='datasets_clean.csv'
df = pd.read_csv(input1)

with st.sidebar:
    i1=st.button('90012')
    i2=st.button('90013')
    i3=st.button('90007')
if i1:
    zipcode('90012',df)
elif i2:
    zipcode('90013',df)
elif i3:
    zipcode('90007',df)
else:
    compare()
