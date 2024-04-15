import csv

main_file = open('./AWS Cloud Workshop (Responses) - Sheet3.csv', 'r')
main_file = csv.reader(main_file)

sample_file = open('./AWS Workshop Day 2 REVIEWSSSSSSSS (Responses) - Sheet1.csv', 'r')
sample_file = csv.reader(sample_file)

names_list = []

for row in sample_file:
    names_list.append(row[0])

print(names_list)