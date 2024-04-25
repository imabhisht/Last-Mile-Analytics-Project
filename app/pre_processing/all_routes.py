import json
import csv
import os
import datetime

directory = '../../data/data/Big Data Project DATA/BRTS/allRouteofBRTS.json'

def main():
    headers = ["route_id","route_code","customer_route_code","route","start_name","end_name","start_stop_code","end_stop_code","start_time","start_time_min","end_time","end_time_min","days","line_type","variant"]
    csv_file = open("../data/brts_all_routes.csv", mode='w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(headers)  

    data = json.load(open(directory, 'r'))

    for entry in data["Data"]:
        route_id = entry["routeId"]
        route_code = entry["routeCode"]
        customer_route_code = entry["customerRouteCode"]
        route = entry["route"]
        start_name = entry["startName"]
        end_name = entry["endName"]
        start_stop_code = entry["startStopCode"]
        end_stop_code = entry["endStopCode"]
        start_time = (entry["startTime"]).split(":")[0]
        start_time_min = (entry["startTime"]).split(":")[1]
        end_time =(entry["endTime"]).split(":")[0]
        end_time_min = (entry["endTime"]).split(":")[1]
        days = entry["days"]
        line_type = entry["linetype"]
        variant = entry["Variant"]

        writer.writerow([route_id, route_code, customer_route_code, route, start_name, end_name, start_stop_code, end_stop_code, start_time, start_time_min, end_time, end_time_min, days, line_type, variant])

    csv_file.close()


if __name__ == "__main__":
    main()