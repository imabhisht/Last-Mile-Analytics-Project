import json
import csv
import os

directory = '../../data/data/Big Data Project DATA/BRTS/Route_Details'


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
        schedule_for_route_id = entry["ScheduleForRouteId"]
        schedule_code = entry["schedulecode"]
        schedule_for_route_code = entry["scheduleForRouteCode"]
        route_code = entry["routeCode"]
        route_name = entry["routeName"]
        route_destination = entry["routeDestination"]
        route_variant = entry["routeVariant"]
        first_stop_code = entry["firstStopCode"]
        last_stop_code = entry["lastStopCode"]
        shift = entry["Shift"]
        start_time = (entry["startTime"]).split(":")[0]
        start_time_min = (entry["startTime"]).split(":")[1]
        end_time = (entry["stopTime"]).split(":")[0]
        end_time_min = (entry["stopTime"]).split(":")[1]
        run_code = entry["runCode"]
        trip_seq_number = entry["tripSeqNumber"]
        duty_code = entry["dutyCode"]
        first_stop_name = entry["firstStopName"]
        last_stop_name = entry["lastStopName"]
        bus_no = entry["busNo"]

        processed_data.append([schedule_for_route_id, schedule_code, schedule_for_route_code, route_code, route_name, route_destination, route_variant, first_stop_code, last_stop_code, shift, start_time, start_time_min, end_time, end_time_min, run_code, trip_seq_number, duty_code, first_stop_name, last_stop_name, bus_no])

    return processed_data

def main():
    headers = ["schedule_for_route_id","schedule_code","schedule_for_route_code", "route_code","route_name","route_destination","route_variant","first_stop_code","last_stop_code","shift","start_time","start_time_min","end_time","end_time_min","run_code","trip_seq_number","duty_code","first_stop_name","last_stop_name","bus_no"]
    csv_file = open("../data/brts_routes_details.csv", mode='w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(headers)  

    filepaths = list_all_file_path()
    for filepath in filepaths:
        data = load_traffic_data(filepath)["Data"]
        processed_data = operation(data)
        for entry in processed_data:
            writer.writerow(entry)

    csv_file.close()


if __name__ == "__main__":
    main()