import streamlit as st
import pandas as pd
import base64
import numpy as np
import pydeck as pdk
import PIL
from PIL import Image
def get_zipcode(store):
    # all str lower case
    store = store.lower()
    try:
        list1 = df[df['Store'] == store].iloc[0].tolist()[2:7]
    except:
        list1 = df_res[df_res['Store'] == store].iloc[0].tolist()[2:7]
    return list1
def main_page(list1):
    st.write("""
     #### Suggested Zipcode base on your selection is
     """)
    t3, t4, t5, t6, t7, t8 = st.columns((0.002, 0.01, 0.002, 0.01, 0.002, 0.01))
    t3.image('img5.png', width=40)
    t4.write(""" ### {}""".format(list1[0]))
    t5.image('img5.png', width=40)
    t6.write(""" ### {}""".format(list1[1]))
    t7.image('img5.png', width=40)
    t8.write(""" ### {}""".format(list1[2]))
    # df2=df[['lat', 'lon']] [(df['PRIMARY NAICS DESCRIPTION'] == 'Full-service restaurants') & (df['ZIP CODE'] == 90012)]
    df2 = df1[['lat', 'lon']][(df1['PRIMARY NAICS DESCRIPTION'] == 'Full-service restaurants')]
    st.map(df2)

## import data and store list
input1='datasets_clean.csv'
df=pd.read_csv('store.csv')
df_res=pd.read_csv('restaurant.csv')
df1 = pd.read_csv(input1)
#get store rows name of data as a list
store_list=df['Store'].tolist()
store_list.append('Resturant')
store_list = [x.title() for x in store_list]
store_list=sorted(store_list)
#resrurant list
res_list=df_res['Store'].tolist()
res_list = [x.title() for x in res_list]
res_list=sorted(res_list)
# set UI style
# title = '<p style="font-family:Fantasy-fonts; color:Black; font-size: 42px;text-align: center; font-weight: bold;"></strong>Locata</strong></p>'
# st.markdown(title, unsafe_allow_html=True)
st.set_page_config(page_title='SWAST - Handover Delays', layout='wide', page_icon=':ambulance:')
t1, t2 = st.columns((0.2, 1))
t1.image('TheSeal.png', width = 120)
t2.title("Locata: "
         "Retail Location Recommendation System")

style = {'font-size': '24px'}

business_type = st.selectbox("Please choose a business type you want to open: ",store_list)

# Result display and map display
if business_type !='select' and business_type !='Resturant':
    str1=str(get_zipcode(business_type))[1:-1]
    y=get_zipcode(business_type)
    main_page(y)
elif business_type =='Resturant':
    res_type = st.selectbox("Resturant type: ", res_list)
    y=get_zipcode(res_type)
    main_page(y)
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
