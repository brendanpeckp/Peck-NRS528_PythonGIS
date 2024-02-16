# # 3. Working with CSV
# # Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa,
# # Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
# #
# # Using Python (csv) calculate the following:
# #
# # Annual average for each year in the dataset.
# # Minimum, maximum and average for the entire dataset.
# # Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November)
# # and Winter (December, January, February).
# # Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

######
## Notes
######
## CSV stands for Comma Seperated Values. These files are easily read by humans and computers. It remains a consistant and
## reliable format.

######
import csv # Allow me the functions to mrite to and from a .csv
with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    # "open" opens the named .csv file.
    # "as" names the opened file as the name following "as".
    # "with" ensures that the .csv is closed after opening.
    # So; with open("x.csv") as example_name:
    csv_reader = csv.reader(daily_co2_csv, delimiter=',')
            # "csv_reader = x" This will set "csv_reader" as equal to the following
            # "csv.reader" the reader takes "population_csv" (equal to "co2-ppm-daily (1).csv") and the delimiter.
            # "csv.reader()" will be able to look at each individual value in the .csv
            # "delimiter=','" sets "," as seperators.
    line_count = 0
    for row in csv_reader:
        # The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object.
        # "If" will test if its following text is true.
        if line_count == 0:
            print("Column names are: " + str(row)) # now the column headers are 0, 1, 2, 3 stored in a string
            line_count += 1
        line_count += 1
        print("Processed " + str(line_count) + " lines.") # tells me if I did this correctly.
## At this point I made this python file capable of reading the csv file and
## I have been able to read the columb headers from the .csv file in this environment.
## Next, I need to pull values from the .csv, do operations with them, then print something like "The average value is x"

### Here I play with an example from class to understand it. Next I will repurpose it for
# # with open("co2-ppm-daily (1).csv") as daily_co2_csv:
# #     next(daily_co2_csv) #skip first line
# #     total = 0
# #     print('total = ' + str(total))
# #     for row in csv.reader(daily_co2_csv):
# #         total += float(row[1]) #1 = 2nd column, in this case, co2 in ppm, remember Python uses zero indexing
# #     print(format(total, 'f')) # format prints as float
# #     print(total) # without we print as engineering notation
# #     # Now look at the data, 3 hundred billion? Ah, we have multiple years..

# # with open("co2-ppm-daily (1).csv") as daily_co2_csv:
# #     next(daily_co2_csv)
# #     average = 0
# #     for row in csv.reader(daily_co2_csv):
# #         average += float(row[1]) / 18766
# #         # average is the variable
# #         # += will add up all values in the columb.
# #         # float will "Convert a string or number to a floating point number, if possible."
# #     print('average daily co2 = ' + format(average, 'f') + ' ppm') # format prints as float

import datetime

with open("co2-ppm-daily (1).csv") as daily_co2_csv:
    next(daily_co2_csv)
    average = 0
    for row in csv.reader(daily_co2_csv):
        average += float(row[1]) / 18766
        # average is the variable
        # += will add up all values in the columb.
        # float will "Convert a string or number to a floating point number, if possible."
    print('average daily co2 = ' + format(average, 'f') + ' ppm') # format prints as float

