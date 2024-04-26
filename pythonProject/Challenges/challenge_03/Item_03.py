# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.


# imports
import csv

# PART 1: Find the annual average for each year in the dataset
print("PART 1")
# Below has two parts. First extract years. Then, extract and average values per year. This process may be used for
# months and seasons if you can specify a list of months or seasons.
# this extracts years
year_list = [] # This is an empty list of years. It will include all years from the csv without duplicates.

with open("co2-ppm-daily (1).csv") as daily_co2_csv: # opens file
    csv_reader = csv.reader(daily_co2_csv, delimiter=',') # understands file as series of lists where ',' is seperator.
    next(csv_reader) # skips the header
    for row in csv_reader: # loops through each list in the csv
        year = row[0].split('-')[0] # identify where in the list the year value is
        if year not in year_list: # test for duplicates before appending to year_list
            year_list.append(year) # append to year_list

print("The dataset covers the following years: " + str(year_list))
print("Average CO2 ppm per year: ")
# this extracts average value per year
for year in year_list: # loop through years
    year_list_output = [] # for each year there will be a list of values created.
    with open("co2-ppm-daily (1).csv") as daily_co2_csv:
        csv_reader = csv.reader(daily_co2_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            year_test = row[0].split('-')[0] # if year in csv is same as year in year_list, run the loop
            if year == year_test:
                year_list_output.append(float(row[1])) # append with the value row (not the year row)
    print(str(year) + ": " + str(sum(year_list_output) / len(year_list_output))) # take the sum of values in the year
    # and divide by the number of values in the year to create yearly average.

# PART 2
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
print("The minimum for entire dataset is: " + str(minimum))
print("The maximum for the entire dataset is: " + str(maximum))
print("The average for entire dataset is: " + str(mean))
#
# # Part 3
# Find seasonal average if Spring (March, April, May), Summer (June, July, August),
# Autumn (September, October, November) and Winter (December, January, February).

spring = ['03', '04', '05']

spring_value = []

with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        month = row[0].split('-')[1] # This specific line of code is what I was misunderstanding. To select a season,
        # I use "row[0] to specify the date field (row 2 is the value field). Then, within that row I split it into
        # three arguements where "-" is the delimiter. I specify that arguement 1 is where we find the month.
        if month in spring:
            spring_value.append(float(row[1]))


spring_value_avg = sum(spring_value) / len(spring_value)

print("Spring avg = " + str(spring_value_avg))

# copy for all seasons

# Part 4
anomaly_list = []
for value in value_list:
    anomaly = (value - mean)
    # print(deviation)
    anomaly_list.append(anomaly)
# print("# 4: The anomaly for each value relative to the mean: " + str(anomaly_list))