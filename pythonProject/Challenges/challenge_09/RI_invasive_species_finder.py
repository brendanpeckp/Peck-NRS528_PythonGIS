# IMPORT MODULES
import arcpy
from arcpy import da
from arcpy import *
import os

# SET WORKSPACE
# Change the below to your own workspace.
######################################################################################
arcpy.env.workspace = r'C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_09'
######################################################################################
workspace = arcpy.env.workspace
print("Workspace directory: " + workspace)

# ESTABLISH INPUT DATA AND ITS FIELDS
inputShapefile = 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
print("Input shapefile: " + str(inputShapefile))

listFields = arcpy.ListFields(inputShapefile)
fields = []
for field in listFields:
    # print(field.name)
    fields.append(field.name)
print("Input shapefile's list of field-names: " + str(fields))

# USE SEARCHCURSOR TO CREATE TWO LISTS OF SHAPES
## List 1: With photos
## List 2: Without photos

field_photo_18 = []

with arcpy.da.SearchCursor(inputShapefile, fields) as cursor:
    for row in cursor:
        if row[10] not in field_photo_18:
            field_photo_18.append(row[10])

print(field_photo_18)
print("There are " + str(len(field_photo_18)) + " records in the 'fieldOther' list.")

photographedExpression = '"photo" = "y"'

arcpy.da.SearchCursor(inputShapefile, photographedExpression, {spatial_reference}, {fields}, {sort_fields})