
#####
# Step 1 - Data Access module
#####

# You can programmatically interact with attribute tables using the data access module. It's easy, fast
# and powerful, allowing you direct access to data with only a few lines of code.

# The code is similar to how we would interact with a CSV file using the CSV package. For example:

# Using data that I obtained from: https://catalog.data.gov/dataset/sandhill-crane-locations-autumn-2013-migration
# lets read in each record, and count how many records there are for crane number 100840:

# import the module
# import csv
# # Open the spceified file and assign it to a variable and close it when it's contained text is finished
# with open(r"Step_1.csv") as crane_csv:
#     # enable this code to read a csv file and understand that commas represent breaks.
#     csv_reader = csv.reader(crane_csv, delimiter=',')
#     # begin an integer to be added to in a line count
#     line_count = 0
#     # this for loop adds 1 to the line count every time the for-loop iterates a crane with the id of 100840.
#     # So, it counts how many records there are for that crane.
#     for row in csv_reader:
#         if row[0] == "100840":
#             line_count += 1
#
# print("There are " + str(line_count) + " csv records for crane 100840.")

# Uncomment the below, now let's now do the same using arcpy.da (arcpy data access module), you could of course
# use select and get count but we are doing it the hard way!:

# import arcpy
# from arcpy import da
#
# line_count_da = 0
# with arcpy.da.SearchCursor("Step_1.csv", ['Crane', 'Time', 'X', 'Y']) as cursor:
#     for row in cursor:
#         if row[0] == 100840:
#             line_count_da += 1
# print("There are " + str(line_count_da) + " arcpy.da records for crane 100840.")


# Task - Using arcpy.da, count how many individual cranes there are in the Step_1.csv data (hint: 5), and
# extract their identification numbers and the number of records for each crane (hint: 100840, 100843, 100853, 100854).

# Think about what you need to do:
#
# 1: Run through each row, pull the crane, add it to a list
import arcpy
from arcpy import da
import os

crane_list = []

with arcpy.da.SearchCursor("Step_1.csv", ['Crane', 'Time', 'X', 'Y']) as cursor:
    for row in cursor:
        if row[0] not in crane_list:
            crane_list.append(row[0])

print(crane_list) # This is a list of all the submission types for a column in a table.
print("There are " + str(len(crane_list)) + " cranes in the crane list.")

# then 2: for each item in your generated list, add it to a dict, count occurrences and then 3: print your len(dict)
# and print dict.

crane_count = {} # This is an empty dict

for crane in crane_list:
    with arcpy.da.SearchCursor("Step_1.csv", ['Crane', 'Time', 'X', 'Y']) as cursor:
        for row in cursor:
            if crane == row[0]:
                if crane not in crane_count.keys():
                    crane_count[crane] = 1
                elif crane in crane_count.keys():
                    crane_count[crane] = crane_count[crane] + 1

print(crane_count)

# Here's some helper code to help you do the count, but first you must generate the list of cranes (hint: append to a
# crane list)!
# crane_count={}
# for i in YOUR_LIST_HERE:
#     if crane == row[0]:
#         if i not in crane_count.keys():
#             crane_count[i]=1  #also: if not i in d
#         else:
#             crane_count[i]+=1