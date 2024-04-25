import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import datetime
import numpy as np
import pydeck as pdk
from st_pages import Page, show_pages, add_page_title
import matplotlib.pyplot as plt
import altair as alt

import functions.map as map_functions
import functions.congestion_metrics as congestion_metrics_functions



st.set_page_config(
    page_title="Statistics | BigData Project",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")


service_type = None
traffic_congestion_data = None
all_locations_data = None
all_routes_data = None
time_hour = None
time_minute = None
time_day = None
specific_station = None
all_stations_list = []

with st.sidebar:
    st.title("Statistics")

    ## Dropdown for selecting the Data
    st.subheader("Serivce Type")
    data = st.selectbox("Select Service", [None, "AMTS", "BRTS"])
    if data:
        service_type = data
        if(service_type == "AMTS"):
            traffic_congestion_data = pd.read_csv("../data/amts_traffic_congestion_data.csv")
            all_locations_data = pd.read_csv("../data/amts_all_loc.csv")
            all_routes_data = pd.read_csv("../data/amts_all_routes.csv")

        if(service_type == "BRTS"):
            traffic_congestion_data = pd.read_csv("../data/brts_traffic_congestion_data.csv")
            all_locations_data = pd.read_csv("../data/brts_all_loc.csv")
            all_routes_data = pd.read_csv("../data/brts_all_routes.csv")

    if service_type:
        ## Dropdown for seleting Time and Day of the week, Default is Current Time and Day
        st.subheader("Customize Time")
        current_time = datetime.datetime.now()
        current_day = current_time.strftime("%A")
        current_hour = current_time.strftime("%H")
        current_minute = current_time.strftime("%M")
        current_time = st.time_input("Select Time", datetime.time(int(9), int(0)))
        current_day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=(datetime.datetime.now().weekday() + 1) % 7 - 1)
        if current_day:
            if(current_day == "Monday"):
                current_day = 1
            if(current_day == "Tuesday"):
                current_day = 2
            if(current_day == "Wednesday"):
                current_day = 3
            if(current_day == "Thursday"):
                current_day = 4
            if(current_day == "Friday"):
                current_day = 5
            if(current_day == "Saturday"):
                current_day = 6
            if(current_day == "Sunday"):
                current_day = 7

        time_hour = current_time.hour
        time_minute = current_time.minute
        time_day = current_day
        print("Time Values: ",time_hour, time_minute, time_day)


    ## Dropdown for selecting Specific Station
    if service_type:
        st.subheader("Customize Station")
        all_stations_list = all_locations_data['station_name'].unique()
        specific_station = st.selectbox("Select Station", all_stations_list)    




col = st.columns((5, 3), gap='medium')

if not service_type:
    col[1].write("Please select a service type from the sidebar")


if service_type:
    with col[0]:
        st.subheader("Station Visualization")    
        icon_data = {
        "url": "https://img.icons8.com/plasticine/100/000000/marker.png",
        "width": 128,
        "height":128,
        "anchorY": 128
    }
        map_all_location_data = map_functions.create_traffic_congestion_map_currently(all_locations_data, traffic_congestion_data, time_hour, time_day)
        map_all_location_data['icon_data'] = None
        for i in map_all_location_data.index:
            map_all_location_data["icon_data"][i] = icon_data

        print(map_all_location_data.head())

        view_state = pdk.ViewState(
            longitude=72.5714,
            latitude=23.0225,
            zoom=11,
            pitch=50
        )

        pdk_layers = [
            pdk.Layer(
                type='IconLayer',
                data=map_all_location_data,
                get_icon='icon_data',
                get_size=4,
                pickable=True,
                size_scale=7,
                get_position='[long,lat]'
            ),
            ## Scatterplot Layer for all the stations
            pdk.Layer(
                type='ScatterplotLayer',
                data=map_all_location_data,
                get_position='[long, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius="scaled_traffic_congestion",
                pickable=True,
                auto_highlight=True
            ),
            ## Scatterplot Layer for the specific station
            pdk.Layer(
                type='ScatterplotLayer',
                data=map_all_location_data[map_all_location_data['station_name'] == specific_station],
                get_position='[long, lat]',
                get_color='[30, 30, 200, 160]',
                get_radius="scaled_traffic_congestion",
                pickable=True,
                auto_highlight=True
            )
            ]

        tooltip = {
        "html": "<b>Station Name:</b> {station_name} <br/> <b>Traffic:</b> {traffic_congestion}%",
        "style": {
                "backgroundColor": "steelblue",
                "color": "white"
        }
        }

        r = pdk.Deck(layers=pdk_layers, initial_view_state=view_state, tooltip=tooltip)
        st.pydeck_chart(r)


        ### Bar Chart for the Traffic Congestion on Stations for the specific time and day
        st.subheader("Traffic Congestion on Stations")


        ### HEAT MAP
        heatmap_merged_data = map_functions.create_traffic_congestion_map_currently(all_locations_data, traffic_congestion_data, time_hour, time_day)
        pivot_data = traffic_congestion_data.pivot_table(index='day', columns='time', values='traffic_congestion', aggfunc='mean')
        print(pivot_data.head())
        fig = px.imshow(pivot_data,
                    labels=dict(x="Hour of the Day", y="Day of the Week", color="Congestion (%)"),
                    x=['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
                    y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    color_continuous_scale='viridis')
        
        st.subheader(f"Average Traffic Congestion: {specific_station}")  
        # Display the heatmap
        st.plotly_chart(fig,theme="streamlit",use_container_width=True)



        



        


    


    with col[1]:
        st.markdown('#### Top Traffic Congestion Stations')

        # current_hour = datetime.datetime.now().hour
        # current_day = datetime.datetime.today().weekday() + 1
        data_current_hour = traffic_congestion_data[traffic_congestion_data['time'] == time_hour]
        data_current_hour = data_current_hour[data_current_hour['day'] == time_day]

        st.dataframe(data_current_hour,
                column_order=("station_name", "traffic_congestion"),
                hide_index=True,
                width=None,
                column_config={
                    "station_name": st.column_config.TextColumn(
                        "Station Name",
                    ),
                    "traffic_congestion": st.column_config.ProgressColumn(
                        "Traffic Congestion",
                        format="%f%%",
                        min_value=0,
                        max_value=100,
                    )
                }, use_container_width=True)
        

        ## Line Chart for the Traffic Congestion at the specific station with proper x and y axis
        station_overall_congestion  = congestion_metrics_functions.traffic_congestion_rates_specific_station_allday(traffic_congestion_data, specific_station)
        print(station_overall_congestion)
        st.subheader(f"Traffic Congestion: {specific_station}")  
        chart = alt.Chart(station_overall_congestion).mark_line().encode(
        x='time',
        y='traffic_congestion'
        ).properties(
            width=600,  # Adjust width as needed
            height=400  # Adjust height as needed
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        )

        # Set axis labels
        chart = chart.configure_axis()

        # Display the Altair chart in Streamlit
        st.altair_chart(chart, use_container_width=True)
        

        



