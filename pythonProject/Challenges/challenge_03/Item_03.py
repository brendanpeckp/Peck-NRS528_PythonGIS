# # Annual average for each year in the dataset.
# # Minimum, maximum and average for the entire dataset.
# # Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
# # Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
#
#
# # imports
import csv, math, time
# from datetime import date
#
# # Part 1
# date_list = []
# with open("co2-ppm-daily (1).csv") as daily_co2_csv:
#     csv_reader = csv.reader(daily_co2_csv, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         date_list.append(row[0])
#     print(date_list)
#
# year = date_list[0].split('-')[0]
# with open("co2-ppm-daily (1).csv") as daily_co2_csv:
#     csv_reader = csv.reader(daily_co2_csv, delimiter=',')
#     next(csv_reader)
#     for argument in date_list:
#         print(year)
# # Part 2
# value_list = []
# with open("co2-ppm-daily (1).csv") as daily_co2_csv:
#     csv_reader = csv.reader(daily_co2_csv, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         (value_list.append(float(row[1])))
#     # print(value_list)
# minimum = min(value_list)
# maximum = max(value_list)
# mean = sum(value_list) / len(value_list)
# print("# 2: The minimum for entire dataset is: " + str(minimum))
# print("# 2: The maximum for the entire dataset is: " + str(maximum))
# print("# 2: The average for entire dataset is: " + str(mean))

# Part 3

year_list = []

with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        year = row[0].split('-')[0]
        if year not in year_list:
            year_list.append(year)

print(year_list)

for year in year_list:
    year_list_output = []
    with open("co2-ppm-daily (1).csv") as daily_co2_csv:
        csv_reader = csv.reader(daily_co2_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            year_test = row[0].split('-')[0]
            if year == year_test:
                year_list_output.append(float(row[1]))
    print(str(year) + ": " + str(sum(year_list_output) / len(year_list_output)))


# Seasonal average if Spring (March, April, May), Summer (June, July, August),

# Autumn (September, October, November) and Winter (December, January, February).





spring = ['03', '04', '05']

spring_value = []

with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        month = row[0].split('-')[1]
        if month in spring:
            spring_value.append(float(row[1]))


spring_value_avg = sum(spring_value) / len(spring_value)

print("Spring avg = " + str(spring_value_avg))
#
# # Part 4
# anomaly_list = []
# for value in value_list:
#     anomaly = (value - mean)
#     # print(deviation)
#     anomaly_list.append(anomaly)
# # print("# 4: The anomaly for each value relative to the mean: " + str(anomaly_list))