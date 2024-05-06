import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

def traffic_congestion_rates_specific_station_allday(traffic_congestion_data, station_name):
    station_data = traffic_congestion_data[traffic_congestion_data['station_name'] == station_name]
    station_data = station_data.groupby('time')['traffic_congestion'].mean().reset_index()
    return station_data
    


    