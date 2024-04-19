# IMPORT MODULES
import arcpy
from arcpy import da
from arcpy import *
import os

print('...')
print("SETUP")
print('...')

# SET WORKSPACE
# Change the below to your own workspace.
######################################################################################
arcpy.env.workspace = r'C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_09'
######################################################################################
workspace = arcpy.env.workspace
print("Workspace directory: " + workspace)

arcpy.env.overwriteOutput = True

# ESTABLISH INPUT DATA AND ITS FIELDS
inputShapefile = 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
print("Input shapefile: " + str(inputShapefile))

listFields = arcpy.ListFields(inputShapefile)
fields = []
for field in listFields:
    # print(field.name)
    fields.append(field.name)
print("Input shapefile's list of field-names: " + str(fields))

# USE SEARCHCURSOR TO CREATE DICTIONARY OF RECORDS WITH AND WITHOUT PHOTOS
# First extract all unique input types for the column
# Then, create a dictionary and add counts for each time a row with an input type is made.

print('...')
print("PART ONE; NUMBER OF PHOTOGRAPHED RECORDS")
print('...')

# Here's me usin SearchCursor to collect unique inputs.
field_photo_18 = []

with arcpy.da.SearchCursor(inputShapefile, fields) as cursor:
    for row in cursor:
        if row[18] not in field_photo_18:
            field_photo_18.append(row[18])

print("There are " + str(len(field_photo_18)) + " record types in the 'photos' field. They are: " + str(field_photo_18))

# Here's me countin the occurences and puttin them in a dict.
photo_count = {}

for y_ in field_photo_18:
    with arcpy.da.SearchCursor(inputShapefile, fields) as cursor:
        for row in cursor:
            if y_ == row[18]:
                if y_ not in photo_count.keys():
                    photo_count[y_] = 1
                elif y_ in photo_count.keys():
                    photo_count[y_] = photo_count[y_] + 1

print("Number of records with and without a photo ('y' for yes and ' ' for no): " + str(photo_count))

print('...')
print("PART TWO; COUNT UNIQUE SPECIES")
print('...')
# Copy the first process from part one; get unique input types from the field/column of 'Species' (row 8)
# Then, instead of counting occurences for each, I need to count number of types.

field_Species_8 = []

with arcpy.da.SearchCursor(inputShapefile, fields) as cursor:
    for row in cursor:
        if row[8] not in field_Species_8:
            field_Species_8.append(row[8])

print("There are " + str(len(field_Species_8)) + " unique species in the 'Species' field. They are: " + str(field_Species_8))

print('...')
print("PART THREE; CREATE SHAPEFILES FOR RECORDS WITH AND WITHOUT PHOTOS")
print('...')

# With photos
points_with_photos = 'points_with_photos.shp'

arcpy.analysis.Select(inputShapefile, points_with_photos, "photo = 'y'")

# without photos
points_without_photos = 'points_without_photos.shp'

arcpy.analysis.Select(inputShapefile, points_without_photos, "photo = ' '")