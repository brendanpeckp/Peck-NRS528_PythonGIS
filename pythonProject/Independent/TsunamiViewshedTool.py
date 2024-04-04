# This tool requires two prepared inputs:
# 1st is World Countries from https://uri.maps.arcgis.com/home/item.html?id=ac80670eb213440ea5899bbf92a04998&sublayer=0
# 2nd is GEM active faults from https://github.com/GEMScienceTools/gem-global-active-faults/tree/master/shapefile
# Both should be clipped to your study area and must be projected in meters.
# Name your Countries vector as "SampleCountires_poly.shp"
# Name your Faults vector as "SampleFaults_lines.shp"

# Table of Contents for Script
## Setup
### Imports
### Overwrite Statement
### Create Temporary Directory
## Data Processing
### Prepare Barrier Features
### Prepare Observation Features
### 2D Viewshed Batch For-Loop
## Cleanup
## Output

print("START SETUP")
import time
setup_startTime = time.time()

import os
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput = True

#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent"
#######################################################################################################################
arcpy.env.workspace = workspace

print("The input data, backup data and script is composed of " + str(len(arcpy.ListFiles("*"))) + " files.")
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

print("SETUP COMPLETED")
setup_endTime = time.time()
setup_elapsedTime = setup_endTime - setup_startTime
print("The setup process took " + str(setup_elapsedTime) + " seconds to run")

print("START DATA PROCESSING")
dataProcessing_startTime = time.time()

print("START PREPARING BARRIER FEATURES")

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

# Save the output and describe output
Land1_ElseNull.save(os.path.join(r"Temp\Land1_ElseNull.tif"))
Land1_ElseNull_Description = arcpy.Describe(os.path.join(r"Temp\Land1_ElseNull.tif"))
print("The name of Test's output is: " + str(Land1_ElseNull_Description.name))
print("The dataset type of Test's output is: " + str(Land1_ElseNull_Description.datasetType))

# Tidy up directory before moving to observation features. Check for success and state completion.
arcpy.Delete_management(os.path.join("Countries_Raster.tif"))
if os.path.exists(os.path.join("Countries_Raster.tif")) is False:
    print("The intermediate data (Countries_Raster.tif) was deleted successfully!")
    print("BARRIER FEATURES COMPLETED")
else:
    print("The intermediate data (Countries_Raster.tif) was NOT deleted successfully.")

print("START PREPARING OBSERVATION FEATURES")

# Erase faultlines that overlap with pixels that represent land.
# Set variables
faults = os.path.join("SampleFaults_lines.shp")
land = Countries_Polygons
oceanFaults = os.path.join(r"Temp\oceanFaults.shp")

# Execute Erase
arcpy.analysis.Erase(faults, land, oceanFaults)

# Dissolve all oceanFaults to one multipart feature.
# Set Variables
# in_features already set as oceanFaults
multipart_oceanFaults = os.path.join(r"Temp\multipart_oceanFaults.shp")

# Execute Dissolve
arcpy.management.Dissolve(oceanFaults, multipart_oceanFaults, "", "", "MULTI_PART", "", "")

# Tidy up temp directory before moving to the loop. Check for success and state completion.
arcpy.Delete_management(os.path.join(r"Temp\oceanFaults.shp"))
if os.path.exists(os.path.join(r"Temp\oceanFaults.shp")) is False:
    print("The intermediate data (oceanFaults.shp) was deleted successfully!")
    print("OBSERVATION FEATURES PREPARED")
else:
    print("The intermediate data (oceanFaults.shp) was NOT deleted successfully.")

# Make a directory for the viewshed output
print("Checking for viewshed output directory...")
if os.path.exists("Viewshed") is False:
    os.mkdir("Viewshed")
    print("The viewshed output directory was created successfully!")
else:
    print("The viewshed output directory was already created.")
Temporary_Directory = os.path.join("Viewshed")
print("The viewshed output directory is named " + str(os.path.join(Temporary_Directory)))

# Start of loop
# Loop code
# for iteration in range x:
############
# Contents of loop confined in here.
# CreateRandomPoints
# Set variables for CreateRandomPoints
out_path = os.path.join(r"Temp")
out_name = os.path.join("observationFeatures")
constraining_feature_class = os.path.join(r"Temp\multipart_oceanFaults.shp")
number_of_points_or_field = 10
minimum_allowed_distance = "1000 Meter"

# Execute CreateRandomPoints
arcpy.management.CreateRandomPoints(out_path, out_name, constraining_feature_class, "", number_of_points_or_field, minimum_allowed_distance, "MULTIPOINT", "")
# Dissolve Points
# 2D Viewshed
toolbox = arcpy.AddToolbox(r"2D_Viewshed_Analysis.tbx")
# Set variables

############
# End of loop
# Combine the outputs of the for loop into a single viewshed.
