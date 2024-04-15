import json
import csv

# Load the JSON data
json_data = '''
{
  "station_name": "Kalupur Railway Station",
  "traffic": [
    "44% busy at 4am.",
    "50% busy at 5am.",
    "56% busy at 6am.",
    "57% busy at 7am.",
    "55% busy at 8am.",
    "46% busy at 9am.",
    "38% busy at 10am.",
    "31% busy at 11am.",
    "28% busy at 12pm.",
    "31% busy at 1pm.",
    "30% busy at 2pm.",
    "30% busy at 3pm.",
    "38% busy at 4pm.",
    "58% busy at 5pm.",
    "77% busy at 6pm.",
    "85% busy at 7pm.",
    "92% busy at 8pm.",
    "95% busy at 9pm.",
    "99% busy at 10pm.",
    "90% busy at 11pm.",
    "68% busy at 12am.",
    "49% busy at 1am.",
    "38% busy at 2am.",
    "36% busy at 3am.",
    "44% busy at 4am.",
    "54% busy at 5am.",
    "62% busy at 6am.",
    "66% busy at 7am.",
    "68% busy at 8am.",
    "62% busy at 9am.",
    "52% busy at 10am.",
    "40% busy at 11am.",
    "35% busy at 12pm.",
    "38% busy at 1pm.",
    "42% busy at 2pm.",
    "41% busy at 3pm.",
    "41% busy at 4pm.",
    "53% busy at 5pm.",
    "69% busy at 6pm.",
    "78% busy at 7pm.",
    "87% busy at 8pm.",
    "91% busy at 9pm.",
    "92% busy at 10pm.",
    "77% busy at 11pm.",
    "55% busy at 12am.",
    "36% busy at 1am.",
    "29% busy at 2am.",
    "32% busy at 3am.",
    "40% busy at 4am.",
    "49% busy at 5am.",
    "55% busy at 6am.",
    "58% busy at 7am.",
    "55% busy at 8am.",
    "48% busy at 9am.",
    "42% busy at 10am.",
    "35% busy at 11am.",
    "35% busy at 12pm.",
    "39% busy at 1pm.",
    "42% busy at 2pm.",
    "40% busy at 3pm.",
    "41% busy at 4pm.",
    "53% busy at 5pm.",
    "70% busy at 6pm.",
    "78% busy at 7pm.",
    "87% busy at 8pm.",
    "91% busy at 9pm.",
    "93% busy at 10pm.",
    "79% busy at 11pm.",
    "55% busy at 12am.",
    "37% busy at 1am.",
    "28% busy at 2am.",
    "29% busy at 3am.",
    "38% busy at 4am.",
    "47% busy at 5am.",
    "52% busy at 6am.",
    "55% busy at 7am.",
    "55% busy at 8am.",
    "49% busy at 9am.",
    "40% busy at 10am.",
    "30% busy at 11am.",
    "27% busy at 12pm.",
    "29% busy at 1pm.",
    "32% busy at 2pm.",
    "32% busy at 3pm.",
    "38% busy at 4pm.",
    "55% busy at 5pm.",
    "74% busy at 6pm.",
    "86% busy at 7pm.",
    "89% busy at 8pm.",
    "87% busy at 9pm.",
    "83% busy at 10pm.",
    "72% busy at 11pm.",
    "52% busy at 12am.",
    "35% busy at 1am.",
    "28% busy at 2am.",
    "29% busy at 3am.",
    "38% busy at 4am.",
    "45% busy at 5am.",
    "49% busy at 6am.",
    "51% busy at 7am.",
    "51% busy at 8am.",
    "47% busy at 9am.",
    "39% busy at 10am.",
    "31% busy at 11am.",
    "29% busy at 12pm.",
    "33% busy at 1pm.",
    "37% busy at 2pm.",
    "39% busy at 3pm.",
    "41% busy at 4pm.",
    "52% busy at 5pm.",
    "66% busy at 6pm.",
    "75% busy at 7pm.",
    "85% busy at 8pm.",
    "91% busy at 9pm.",
    "92% busy at 10pm.",
    "Currently 69% busy, usually 80% busy.",
    "56% busy at 12am.",
    "38% busy at 1am.",
    "30% busy at 2am.",
    "31% busy at 3am.",
    "44% busy at 4am.",
    "51% busy at 5am.",
    "55% busy at 6am.",
    "56% busy at 7am.",
    "53% busy at 8am.",
    "45% busy at 9am.",
    "38% busy at 10am.",
    "32% busy at 11am.",
    "31% busy at 12pm.",
    "36% busy at 1pm.",
    "39% busy at 2pm.",
    "39% busy at 3pm.",
    "43% busy at 4pm.",
    "59% busy at 5pm.",
    "78% busy at 6pm.",
    "88% busy at 7pm.",
    "94% busy at 8pm.",
    "96% busy at 9pm.",
    "94% busy at 10pm.",
    "80% busy at 11pm.",
    "56% busy at 12am.",
    "39% busy at 1am.",
    "33% busy at 2am.",
    "37% busy at 3am.",
    "48% busy at 4am.",
    "53% busy at 5am.",
    "56% busy at 6am.",
    "58% busy at 7am.",
    "57% busy at 8am.",
    "53% busy at 9am.",
    "45% busy at 10am.",
    "37% busy at 11am.",
    "33% busy at 12pm.",
    "37% busy at 1pm.",
    "41% busy at 2pm.",
    "40% busy at 3pm.",
    "41% busy at 4pm.",
    "54% busy at 5pm.",
    "72% busy at 6pm.",
    "83% busy at 7pm.",
    "93% busy at 8pm.",
    "98% busy at 9pm.",
    "100% busy at 10pm.",
    "87% busy at 11pm.",
    "64% busy at 12am.",
    "46% busy at 1am.",
    "40% busy at 2am.",
    "42% busy at 3am."
  ]
}
'''

def convert_time_to_24hour_format(time):
    if "am" in time:
        if int(time.split("am")[0]) == 12:
            return "0"
        return time.split("am")[0]
    if "pm" in time:

        if int(time.split("pm")[0]) == 12:
            return time.split("pm")[0]
        return str(int(time.split("pm")[0]) + 12)

data = json.loads(json_data)

# Extract the traffic congestion data
traffic_data = data["traffic"]

# Define the headers for the CSV file
headers = ["day","time", "traffic_congestion"]

# Define the file name for the CSV file
csv_file = "traffic_congestion_data.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the headers
    writer.writerow(headers)

    start_time = traffic_data[0].split(" busy")[1].split("at ")[1]
    
    day_counter = 0
    prevTime = ""

    for entry in traffic_data:
        ## Handle Currently
        if(entry.startswith("Currently")):
            time = str(prevTime+1)
            continue

        elif(entry.split(" busy")[1].split("at ")[1] == start_time):
            day_counter += 1

        print(convert_time_to_24hour_format(entry.split(" busy")[1].split("at ")[1]) , day_counter)
        # Extract time and congestion percentage
        # time = entry.split(" busy")[0].split("at ")[0]
        # congestion = entry.split(" busy")[0].split("at ")[0]
        
        # # Append to CSV
        # writer.writerow([time, congestion])

print("CSV file has been created successfully.")
