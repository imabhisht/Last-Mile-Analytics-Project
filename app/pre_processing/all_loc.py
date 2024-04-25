import json
import csv
import os

directory = '../../data/data/Big Data Project DATA/AMTS/all_loc.json'

def main():
    headers = ["station_name","long","lat"]
    csv_file = open("../data/amts_all_loc.csv", mode='w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(headers)  

    data = json.load(open(directory, 'r'))

    for entry in data["all_station"]:
        writer.writerow([entry["station_name"], entry["loacation"]["longitude"], entry["loacation"]["latitude"]])

    csv_file.close()


if __name__ == "__main__":
    main()