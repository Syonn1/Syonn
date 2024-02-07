# home.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_extras.stylable_container import stylable_container
from st_pages import Page, show_pages

st.set_page_config(page_title="Hotel Prediction",
                   page_icon=":hotel:",
                   initial_sidebar_state="expanded",
                   )

df = pd.read_csv('hotel_booking_fixed.csv')

st.title('Data Visualization :bar_chart:')

grafik1 = st.container()
grafik2 = st.container()
grafik3 = st.container() 
grafik4 = st.container()

# Sidebar
with st.sidebar:
    st.title(":airplane: About the dataset")
    st.markdown("Pernahkah kamu bertanya-tanya kapan waktu terbaik untuk memesan kamar hotel? Atau berapa lama waktu menginap optimal agar mendapatkan tarif harian terbaik? Bagaimana jika Anda ingin memprediksi apakah suatu hotel kemungkinan besar menerima jumlah permintaan khusus yang tidak proporsional?")
    st.markdown("Dataset pemesanan hotel ini dapat membantu Anda menjelajahi pertanyaan-pertanyaan tersebut!")
    show_pages([
        Page("home.py", "Data Visualization", ":bar_chart:"),
        Page("app.py", "Prediction", ":rocket:"),
    ])

#grafik
with grafik1:
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 10px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
        resort_hotel_df = df.loc[(df["hotel"] == "Resort Hotel") & (df["is_canceled"] == 0)]
        city_hotel_df =df.loc[(df["hotel"] == "City Hotel") & (df["is_canceled"] == 0)]
        st.header("How does the price vary over seasons?")
        tab1, tab2 = st.tabs(["in City", "in Resort"])
        with tab1:
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.barplot(data=city_hotel_df, x='Seasons', y='adr', color='skyblue', edgecolor='black', alpha=0.7)
            #plt.title("Average Room price per night and person over the season in City", fontsize=16)
            plt.xlabel("Seasons", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            st.pyplot(fig)
        with tab2:
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.barplot(data = resort_hotel_df, x='Seasons' , y ='adr', color='skyblue', edgecolor='black', alpha=0.7)
            #plt.title("Average Room price per night and person over the season in Resort", fontsize=16)
            plt.xlabel("Seasons", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            st.pyplot(fig)

with grafik2:
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #000000; /* Warna background */
               padding: 10px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
        resort_month=resort_hotel_df.groupby(["arrival_date_month"])["adr"].mean().reset_index()
        city_month=city_hotel_df.groupby(["arrival_date_month"])["adr"].mean().reset_index()
        ordered_months = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]
        resort_month.index = pd.CategoricalIndex(resort_month["arrival_date_month"],categories = ordered_months,ordered=True)
        city_month.index = pd.CategoricalIndex(city_month["arrival_date_month"],categories = ordered_months,ordered=True)
        city_month = city_month.sort_index()
        resort_month = resort_month.sort_index()
        st.header("How does the price per night vary over months?")
        tab1, tab2 = st.tabs(["in City", "in Resort"])
        with tab1:
            plt.title('Average Daily Rate by Month in City')
            plt.figure(figsize=(10, 6))
            sns.barplot(data=city_month, x='arrival_date_month', y='adr')
            plt.xlabel("Month in city", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            st.pyplot(plt)
        with tab2:
            plt.title('Average Daily Rate by Month in Resort')
            plt.figure(figsize=(10, 6))
            sns.barplot(data=resort_month, x='arrival_date_month', y='adr')
            plt.xlabel("Month in resort", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            st.pyplot(plt)
    
with grafik3:
    with stylable_container(
    key="container_with_border",
        css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #000000; /* Warna background */
               padding: 0px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
        resort_room=resort_hotel_df.groupby(["reserved_room_type"])["adr"].mean().reset_index()
        city_room=city_hotel_df.groupby(["reserved_room_type"])["adr"].mean().reset_index()
        ordered_room = ["A","B","C","D","E","F","G","H"]
        resort_room.index = pd.CategoricalIndex(resort_room["reserved_room_type"],categories = ordered_room,ordered=True)
        city_room.index = pd.CategoricalIndex(city_room["reserved_room_type"],categories = ordered_room,ordered=True)
        resort_room = resort_room.sort_index()
        city_room = city_room.sort_index()

        st.header("How does the price per night vary depends on Room Type?")
        tab1, tab2 = st.tabs(["in City", "in Resort"])
        with tab1:
            plt.title('Average Daily Rate by Reserved Room Type in City Hotel')
            plt.figure(figsize=(5, 3))
            sns.barplot(data=city_room, x='reserved_room_type', y='adr')
            plt.xlabel("Room type in city", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            st.pyplot(plt)
        with tab2:
            plt.title('Average Daily Rate by Reserved Room Type in resort Hotel')
            plt.figure(figsize=(5, 3))
            sns.barplot(data=resort_room, x='reserved_room_type', y='adr')
            plt.xlabel("Room type in resort", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            st.pyplot(plt)

with grafik4:
    with stylable_container(
    key="container_with_border",
        css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #000000; /* Warna background */
               padding: 0px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
        st.header("Average By Market Segment And Room type")
        tab1, tab2 = st.tabs(["in City", "in Resort"])
        with tab1:
            plt.title('Average Daily Rate by Market Segment and Reserved Room Type in City Hotel')
            plt.figure(figsize=(12, 8))
            sns.barplot(data=city_hotel_df, x='market_segment', y='adr', hue='reserved_room_type')
            plt.xlabel("Market segment for city", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            plt.legend(title='Reserved Room Type')
            st.pyplot(plt)
        with tab2:
            plt.title('Average Daily Rate by Market Segment and Reserved Room Type in Resort Hotel')
            plt.figure(figsize=(12, 8))
            sns.barplot(data=resort_hotel_df, x='market_segment', y='adr', hue='reserved_room_type')
            plt.xlabel("Market segment for resort", fontsize=16)
            plt.ylabel("Price", fontsize=16)
            plt.legend(title='Reserved Room Type')
            st.pyplot(plt)