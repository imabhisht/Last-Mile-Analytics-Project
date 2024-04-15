import json
import csv
import os

directory = '../../data/data/Big Data Project DATA/BRTS/Traffic Data'


def convert_time_to_24hour_format(time):
    if "am" in time:
        if int(time.split("am")[0]) == 12:
            return "0"
        return time.split("am")[0]
    if "pm" in time:

        if int(time.split("pm")[0]) == 12:
            return time.split("pm")[0]
        return str(int(time.split("pm")[0]) + 12)

def load_traffic_data(filepath):
    with open(filepath, 'r') as file:
        json_data = json.load(file)
    
    return json_data


def list_all_file_path():
    filepaths = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            filepaths.append(filepath)
    
    return filepaths

def operation(data):
    processed_data = []
    station_name = data["station_name"]
    traffic_data = data["traffic"]
    # start_time = traffic_data[0].split(" busy")[1].split("at ")[1]
    day_counter = 6
    prevTime = 0

    for entry in traffic_data:
        if(entry.startswith("Currently")):
            congestion = entry.split("Currently ")[1].split("% busy, usually ")[0]
            time = (time + 1) % 24
            if(time == 0):
                day_counter = (day_counter + 1) % 8 if day_counter != 7 else 1

        else:
            congestion = entry.split(" busy")[0].split("at ")[0]
            time = int(convert_time_to_24hour_format(entry.split(" busy")[1].split("at ")[1]))
            if(time == 0 or (time > 12 and prevTime < 12)):
                day_counter = (day_counter + 1) % 8 if day_counter != 7 else 1

        prevTime = time
        processed_data.append([station_name,day_counter, time, congestion.split("%")[0]])

    return processed_data

def main():
    headers = ["station_name","day","time", "traffic_congestion"]
    csv_file = open("../data/brts_traffic_congestion_data.csv", mode='w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(headers)  

    filepaths = list_all_file_path()
    for filepath in filepaths:
        data = load_traffic_data(filepath)
        print(data["station_name"])
        processed_data = operation(data)
        for entry in processed_data:
            writer.writerow(entry)

    csv_file.close()


if __name__ == "__main__":
    main()