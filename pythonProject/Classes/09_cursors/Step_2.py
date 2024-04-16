
#####
# Step 2 - Data Access module - Searching for values using a cursor.
#####

# You can add in an expression to query your data as part of the cursor, which can
# greatly ease your interaction with the files, however, there are some considerations
# principally, the formatting of an expression:

# import arcpy
#
# input_shp = r'C:\Peck_NRS528_PythonGIS\pythonProject\Classes\09_cursors\Step_2_Data\Places.shp'
# fields = ['code', 'population', 'name', 'SHAPE@XY']
#
# expression = """"population" > 30000"""  # The formatting of an expression is a bit messy...
# expression = arcpy.AddFieldDelimiters(input_shp, "population") + " > 30000"  # Cleaner and easier to code
#
# with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
#     for row in cursor:
#         print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
#         # Side note: XY location data is provided as a tuple, and you need to be specific to extract it correctly:
#         print(u'x = {0}, y = {1}'.format(row[3][0], row[3][1]))

# # Task a - Correct the above code to provide all the detail for each output on a single line rather than 2 lines:

# import arcpy
#
# input_shp = r'C:\Peck_NRS528_PythonGIS\pythonProject\Classes\09_cursors\Step_2_Data\Places.shp'
# fields = ['code', 'population', 'name', 'SHAPE@XY']
#
# expression = arcpy.AddFieldDelimiters(input_shp, "population") + " > 30000"  # Cleaner and easier to code
#
# with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
#     for row in cursor:
#         print(u'{0}, {1}, {2}, x = {0}, y = {1}'.format(row[0], row[1], row[2], row[3][0], row[3][1]))

# Task b - Using the above code, copy it and paste it below, select only place names that begin with the
# # letter S (See https://pro.arcgis.com/en/pro-app/help/mapping/navigation/sql-reference-for-elements-used-in-query-expressions.htm).
# # For bonus points, count how many there are (hint 53).

import arcpy

input_shp = r'C:\Peck_NRS528_PythonGIS\pythonProject\Classes\09_cursors\Step_2_Data\Places.shp'
fields = ['code', 'population', 'name', 'SHAPE@XY']

expression = arcpy.AddFieldDelimiters(input_shp, "name") + " LIKE 'S%'"  # Cleaner and easier to code
count = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        count = count + 1

print("There are " + str(count) + " towns that begin with the letter s.")
