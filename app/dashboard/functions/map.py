import pandas as pd
import datetime
import numpy as np

def scale_traffic_congestion(traffic_congestion):
    if traffic_congestion < 10:
        return traffic_congestion * 1
    elif 10 <= traffic_congestion < 30:
        return traffic_congestion * 2.5
    elif 30 <= traffic_congestion < 50:
        return traffic_congestion * 3.5
    elif 50 <= traffic_congestion < 70:
        return traffic_congestion * 5
    elif 70 <= traffic_congestion < 90:
        return traffic_congestion * 7.53 
    else:
        return traffic_congestion
    
def create_traffic_congestion_map_currently(station_data, traffic_data, time_hour, time_day):
    merged_data = pd.merge(station_data, traffic_data, on='station_name', how='inner')
    merged_data = merged_data[(merged_data['day'] == time_day) & (merged_data['time'] == time_hour)]
    merged_data['scaled_traffic_congestion'] = merged_data['traffic_congestion'].apply(scale_traffic_congestion)
    # print(merged_data.head())

    return merged_data