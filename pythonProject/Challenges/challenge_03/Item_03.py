# imports
import csv, math, time
from datetime import date

# Part 1
date_list = []
with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        date_list.append(row[0])
    print(date_list)

year = date_list[0].split('-')[0]
with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
    next(csv_reader)
    for argument in date_list:
        print(year)
# Part 2
value_list = []
with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        (value_list.append(float(row[1])))
    # print(value_list)
minimum = min(value_list)
maximum = max(value_list)
mean = sum(value_list) / len(value_list)
print("# 2: The minimum for entire dataset is: " + str(minimum))
print("# 2: The maximum for the entire dataset is: " + str(maximum))
print("# 2: The average for entire dataset is: " + str(mean))

# Part 4
anomaly_list = []
for value in value_list:
    anomaly = (value - mean)
    # print(deviation)
    anomaly_list.append(anomaly)
# print("# 4: The anomaly for each value relative to the mean: " + str(anomaly_list))