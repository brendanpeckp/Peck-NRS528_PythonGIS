# This tool requires two prepared inputs:
# 1st is World Countries from https://uri.maps.arcgis.com/home/item.html?id=ac80670eb213440ea5899bbf92a04998&sublayer=0
# 2nd is GEM active faults from https://github.com/GEMScienceTools/gem-global-active-faults/tree/master/shapefile
# Both should be clipped to your study area and must be projected in meters.
# Name your Countries vector as "SampleCountires_poly.shp"
# Name your Faults vector as "SampleFaults_lines.shp"

print("START SETUP")

import os
import arcpy
from arcpy import env
from arcpy.sa import *
import time

arcpy.env.overwriteOutput = True

#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent"
#######################################################################################################################
arcpy.env.workspace = workspace

print("The input data  and script is composed of " + str(len(arcpy.ListFiles("*"))) + " files.")
print("Those files are: " + str(arcpy.ListFiles("*")))

# Create a temporary directory to be deleted later.
print("Checking for temporary directory...")
if os.path.exists("Temp") is False:
    os.mkdir("Temp")
    print("The temporary directory was created successfully!")
else:
    print("The temporary directory was already created.")
Temporary_Directory = os.path.join("Temp")
print("The temporary directory is named " + str(os.path.join(Temporary_Directory)))

print("START DATA PROCESSING")

# Convert Countries_Polygons to raster via Feature to Raster. Output as Countries_Raster
# Set local variables
Countries_Polygons = os.path.join("SampleCountires_poly.shp")
Countries_Raster = os.path.join("Countries_Raster.tif")
cellSize = 50000
field = "COUNTRY"

# Run FeatureToRaster and describe output
arcpy.conversion.FeatureToRaster(Countries_Polygons, field, Countries_Raster, cellSize)
Countries_Raster_Description = arcpy.Describe(os.path.join("Countries_Raster.tif"))
print("The name of FeatureToRaster's output is: " + str(Countries_Raster_Description.name))
print("The dataset type of FeatureToRaster's output is: " + str(Countries_Raster_Description.datasetType))
# Set Countries_Raster to be equal to 1 using Test Output as Land1_ElseNull
# Set local variables
TestinRaster = os.path.join("Countries_Raster.tif")
inWhereClause = "VALUE > 1"


# Execute Test
Land1_ElseNull = Test(TestinRaster, inWhereClause)

# Save the output
Land1_ElseNull.save()