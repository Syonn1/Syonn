import numpy as np
import pandas as pd
import streamlit as st 
import joblib

classifier=joblib.load('Hotel Prediction model.pkl')
st.set_page_config(page_title="Hotel Prediction",
                   page_icon=":hotel:",
                   initial_sidebar_state="expanded",
                   )
with st.sidebar:
    st.title(":airplane: About the dataset")
    st.markdown("Pernahkah kamu bertanya-tanya kapan waktu terbaik untuk memesan kamar hotel? Atau berapa lama waktu menginap optimal agar mendapatkan tarif harian terbaik? Bagaimana jika Anda ingin memprediksi apakah suatu hotel kemungkinan besar menerima jumlah permintaan khusus yang tidak proporsional?")
    st.markdown("Dataset pemesanan hotel ini dapat membantu Anda menjelajahi pertanyaan-pertanyaan tersebut!")

def welcome():
    return "Welcome All"


def predict_hotel(hotel,lead_time,stays_in_weekend_nights,stays_in_week_nights,market_segment,distribution_channel,is_repeated_guest,previous_cancellations,previous_bookings_not_canceled,reserved_room_type,booking_changes,deposit_type,customer_type,total_of_special_requests,Total_Guests,Seasons,Total_Days):
    prediction=classifier.predict(pd.DataFrame({'hotel':[hotel],'lead_time':[lead_time],'stays_in_weekend_nights':[stays_in_weekend_nights],'stays_in_week_nights':[stays_in_week_nights],'market_segment':[market_segment],'distribution_channel':[distribution_channel],'is_repeated_guest':[is_repeated_guest],'previous_cancellations':[previous_cancellations],'previous_bookings_not_canceled':[previous_bookings_not_canceled],'reserved_room_type':[reserved_room_type],'booking_changes':[booking_changes],'deposit_type':[deposit_type],'customer_type':[customer_type],'total_of_special_requests':[total_of_special_requests],'Total_Guests':[Total_Guests],'Seasons':[Seasons],'Total_Days':[Total_Days]}))
    print(prediction)
    label = ['Canceled','Check-Out',]
    return label[prediction[0]]
  
      
def main():
    st.title("Hotel")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction Hotel App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    hotel_options = ["City Hotel", "Resort Hotel"]
    hotel = st.selectbox("Hotel", hotel_options)

    lead_time = st.text_input("Lead Time")
    stays_in_weekend_nights = st.text_input("Stays In weekend Nights")
    stays_in_week_nights = st.text_input("Stays In Week Nights")

    market_options=["Online TA", "Online TA/TO", "Direct", "Groups", "Corporate", "Aviation", "Complementary"]
    market_segment = st.selectbox("Market Segment", market_options)

    distribution_options=["TA/TO", "Direct", "Corporate", "GDS"]
    distribution_channel = st.selectbox("Distribution Channel", distribution_options)
    
    is_repeated_guest = st.text_input("Is Repeated Guest (Ex,0 or 1)")
    previous_cancellations = st.text_input("Previous Cancellations")
    previous_bookings_not_canceled = st.text_input("Previous Bookings Not Canceled")
    
    room_options=["A", "B", "C", "D", "E", "F", "G", "H"]
    reserved_room_type = st.selectbox("Reserved Room Type", room_options)

    booking_changes = st.text_input("Booking Changes")

    deposite_options=["No Deposit", "Non Refund", "Refundable"]
    deposit_type = st.selectbox("Deposit Type", deposite_options)

    customer_options=["Transient", "Transient-Party", "Contract", "Group"]
    customer_type = st.selectbox("Customer Type", customer_options)

    total_of_special_requests = st.text_input("Total Of Special Requests")
    Total_Guests = st.text_input("Total Guests")

    seasons_options=["Summer", "Spring", "Autumn", "Winter"]
    Seasons = st.selectbox("Season", seasons_options)
    Total_Days = st.text_input("Total Days")
    result=""
    if st.button("Predict"):
        result=predict_hotel(hotel,lead_time,stays_in_weekend_nights,stays_in_week_nights,market_segment,distribution_channel,is_repeated_guest,previous_cancellations,previous_bookings_not_canceled,reserved_room_type,booking_changes,deposit_type,customer_type,total_of_special_requests,Total_Guests,Seasons,Total_Days)
    st.success('The Hotel is {}'.format(result))
    if st.button("About"):
        st.text("S. Yonn")
        st.text("Built with Streamlit")

        
if __name__=='__main__':
    main()        
