# This tool requires two prepared inputs:
# 1st is World Countries from https://uri.maps.arcgis.com/home/item.html?id=ac80670eb213440ea5899bbf92a04998&sublayer=0
# 2nd is GEM active faults from https://github.com/GEMScienceTools/gem-global-active-faults/tree/master/shapefile
# Both should be clipped to your study area and must be projected in meters.
# Reset the variable "Countries_Polygons" to your countries data.
# Reset the variable "faults" to your seismic fault data.

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

import os
import arcpy
from arcpy.sa import *

arcpy.env.overwriteOutput = True

#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent"
#######################################################################################################################
arcpy.env.workspace = workspace

# Create a temporary directory to be deleted later.
print("Checking for temporary directory...")
if os.path.exists("Temp") is False:
    os.mkdir("Temp")
    print("The temporary directory was created successfully!")
else:
    print("The temporary directory was already created.")
Temporary_Directory = "Temp"
print("The temporary directory is named " + str(Temporary_Directory))

# Convert Countries_Polygons to raster via Feature to Raster. Output as Countries_Raster
# Set local variables
Countries_Polygons = "SampleCountires_poly.shp"
Countries_Raster = r"Temp\Countries_Raster.tif"
cellSize = 50000
field = "COUNTRY"

# Run FeatureToRaster and describe output
arcpy.conversion.FeatureToRaster(Countries_Polygons, field, Countries_Raster, cellSize)
Countries_Raster_Description = arcpy.Describe(r"Temp\Countries_Raster.tif")
print("The name of FeatureToRaster's output is: " + str(Countries_Raster_Description.name))
print("The dataset type of FeatureToRaster's output is: " + str(Countries_Raster_Description.datasetType))
# Set Countries_Raster to be equal to 1 using Test Output as Land1_ElseNull
# Set local variables
TestinRaster = r"Temp\Countries_Raster.tif"
inWhereClause = "VALUE > 1"

# Execute Test
Land1_ElseNull = Test(TestinRaster, inWhereClause)

# Save the output and describe output
Land1_ElseNull.save(r"Temp\Land1_ElseNull.tif")
Land1_ElseNull_Description = arcpy.Describe(r"Temp\Land1_ElseNull.tif")
print("The name of Test's output is: " + str(Land1_ElseNull_Description.name))
print("The dataset type of Test's output is: " + str(Land1_ElseNull_Description.datasetType))

# Tidy up directory before moving to observation features. Check for success and state completion.
arcpy.Delete_management("Countries_Raster.tif")
if os.path.exists("Countries_Raster.tif") is False:
    print("The intermediate data (Countries_Raster.tif) was deleted successfully!")
else:
    print("The intermediate data (Countries_Raster.tif) was NOT deleted successfully.")

# Erase faultlines that overlap with pixels that represent land.
# Set variables
faults = "SampleFaults_lines.shp"
land = Countries_Polygons
oceanFaults = r"Temp\oceanFaults.shp"

# Execute Erase
arcpy.analysis.Erase(faults, land, oceanFaults)

# Dissolve all oceanFaults to one multipart feature.
# Set Variables
# in_features already set as oceanFaults
multipart_oceanFaults = r"Temp\multipart_oceanFaults.shp"

# Execute Dissolve
arcpy.management.Dissolve(oceanFaults, multipart_oceanFaults, "", "", "MULTI_PART", "", "")

# Tidy up temp directory before moving to the loop. Check for success and state completion.
arcpy.Delete_management(r"Temp\oceanFaults.shp")
if os.path.exists(r"Temp\oceanFaults.shp") is False:
    print("The intermediate data (oceanFaults.shp) was deleted successfully!")
else:
    print("The intermediate data (oceanFaults.shp) was NOT deleted successfully.")

# Make a directory for the viewshed output
# print("Checking for viewshed output directory...")
# if os.path.exists("Viewshed") is False:
#     os.mkdir("Viewshed")
#     print("The viewshed output directory was created successfully!")
# else:
#     print("The viewshed output directory was already created.")

# Set variables for CreateRandomPoints
# out_name = r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent\Temp\observationFeatures.shp"
# constraining_feature_class = r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent\Temp\multipart_oceanFaults.shp"
# number_of_points_or_field = 10
# minimum_allowed_distance = "1000 Meter"

# Begin Loop
############
for iteration in range(50):
    # unique ID
    unique_id = iteration
    # Create unique directories
    print("Checking for viewshed output directory...")
    if os.path.exists(f"Viewshed_{unique_id}") is False:
        os.mkdir(f"Viewshed_{unique_id}")
        print(f"The viewshed_{unique_id} output directory was created successfully!")
    else:
        print(f"The viewshed_{unique_id} output directory was already created.")
    # Run CreateRandomPoints
    arcpy.management.CreateRandomPoints("Temp", "observationPoints.shp", r"Temp\multipart_oceanFaults.shp", "",
                                        10, "1000 Meter",
                                        "POINT", "")
    # Dissolve Random Points to a single multipart feature

    arcpy.Dissolve_management(r"Temp\observationPoints.shp",
                              r"Temp\observationMultiPoints.shp",
                              "", "", "MULTI_PART", "", "")
    # 2D Viewshed
    toolbox = arcpy.AddToolbox(r"2D_Viewshed_Analysis.tbx")
    # Set variables and run the 2D Script
    # toolbox.Script(r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent\Temp\observationMultiPoints.shp", r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent\Temp\Land1_ElseNull.tif", 50000, r"C:\Peck_NRS528_PythonGIS\pythonProject\Independent\Viewshed")
    toolbox.Script(r"Temp\observationMultiPoints.shp", r"Temp\Land1_ElseNull.tif", 50000, f"Viewshed_{unique_id}")
############
# End of loop
# Combine the outputs of the for loop into a single viewshed.