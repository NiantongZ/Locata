import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
input1='test/datasets_clean.csv'
st.title("Locata")
st.subheader("Retail location recommendation")

with st.sidebar:
    hobby = st.selectbox("Business type: ",
                         ['select','Restaurant', 'Personal Service', 'Jewelry Store'])
    income = st.selectbox("Target customer income range",
                          ['select','<20,000', '20,000-50,000', '50,000-10,000', '>10,000'])

    Rental_range = st.selectbox("Area average house value",
                                ['select','<400,000', '40,000-70,000', '70,000-100,000', '>100,000'])

    status = st.radio("Select customer resource: ", ('Both','Online', 'in person'))

#st.write('You selected business type:', hobby,', income:',income,', rental range: ',Rental_range,', Customer resource: ',status)
def test(a,b,c,d):
    x='90012,'+'90013,'+'90007'
    return x



if hobby !='select' and income!='select' and Rental_range!='select':
    st.write('Suggested Zipcode base on your selection is ',test(hobby,income,Rental_range,status))
    df = pd.read_csv(input1)
    # df2=df[['lat', 'lon']] [(df['PRIMARY NAICS DESCRIPTION'] == 'Full-service restaurants') & (df['ZIP CODE'] == 90012)]
    df2 = df[['lat', 'lon']][(df['PRIMARY NAICS DESCRIPTION'] == 'Full-service restaurants')]
    st.map(df2)
else:
    st.write('Please select your business information to get suggested zipcode')

    

# def threadFunc():
#     time.sleep(wait_second)
#     keyboard.press_and_release('ctrl+w')
#
#
# if st.button('test'):
#     th = threading.Thread(target=threadFunc)
#     th.start()
#     # address of streamlit page that you want to open after clicking button
#     os.system('D:')
#     os.system('cd python\Scripts')
#     os.system(r"streamlit run D:\ui\login.py")
#     th.join()
