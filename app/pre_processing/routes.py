import json
import csv
import os

directory = '../../data/data/Big Data Project DATA/AMTS/Routes'


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

    for entry in data:
        if(entry):
            schedule_id = entry["scheduleId"]
            schedule_for_route_code = entry["scheduleForRouteCode"]
            schedule_for_stop_on_route_code = entry["scheduleForStopOnRouteCode"]
            stop_code = entry["stopCode"]
            arrival_time = (entry["arrivalTime"]).split(":")[0]
            arrival_time_min = (entry["arrivalTime"]).split(":")[1]
            departure_time = (entry["departureTime"]).split(":")[0]
            departure_time_min = (entry["departureTime"]).split(":")[1]
            stop_type = entry["stopType"]
            short_stop_name = entry["shortStopName"]
            route_code = entry["routeCode"]
            route = entry["route"]
            lang = entry["position"]["stopLatitude"]
            long = entry["position"]["stopLongitude"]
            geometric_position = entry["geometricPosition"]

            processed_data.append([schedule_id, schedule_for_route_code, schedule_for_stop_on_route_code, stop_code, arrival_time, arrival_time_min, departure_time, departure_time_min, stop_type, short_stop_name, route_code, route, lang, long, geometric_position])

    return processed_data

def main():
    headers = ["schedule_id","schedule_for_route_code","schedule_for_stop_on_route_code","stop_code","arrival_time","arrival_time_min","departure_time","departure_time_min","stop_type","short_stop_name","route_code","route","lang","long","geometric_position"]
    csv_file = open("../data/amts_routes.csv", mode='w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(headers)  

    filepaths = list_all_file_path()
    for filepath in filepaths:
        print(filepath)
        data = load_traffic_data(filepath)
        if "Data" in data:
            data = data["Data"]
        else:
            continue
        processed_data = operation(data)
        for entry in processed_data:
            writer.writerow(entry)

    csv_file.close()


if __name__ == "__main__":
    main()