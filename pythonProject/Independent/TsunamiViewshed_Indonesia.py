# This tool requires two prepared inputs:
# 1st is World Countries from https://uri.maps.arcgis.com/home/item.html?id=ac80670eb213440ea5899bbf92a04998&sublayer=0
# 2nd is GEM active faults from https://github.com/GEMScienceTools/gem-global-active-faults/tree/master/shapefile
# Both should be clipped to your study area and must be projected in meters.
# Reset the variable "Countries_Polygons" to your countries data.
# Reset the variable "faults" to your seismic fault data.

# Things you should change in this script:
#! The variable named "cellSize"; depending on how fast or granular you want to run this script, you should change the
#! integer represented by the variable "cellSize". I have set it to 50,000 by defalt, but I want my output to be a bit more granular.
#@ Input data
#$ Iterations; For the for loop you can change the integer to get more or less iterations of the loop
#% Number of cells to expand by in the Expand tool.

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
import time
start_time = time.time()
import os
import arcpy
from arcpy.sa import *
import shutil

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
Countries_Polygons = "IndonesiaCountries_DGM95UTMz50S.shp"
Countries_Raster = r"Temp\Countries_Raster.tif"
cellSize = 100000
field = "COUNTRY"

# Run FeatureToRaster and describe output
arcpy.conversion.FeatureToRaster(Countries_Polygons, field, Countries_Raster, cellSize)
Countries_Raster_Description = arcpy.Describe(r"Temp\Countries_Raster.tif")
print("The name of FeatureToRaster's output is: " + str(Countries_Raster_Description.name))
print("The dataset type of FeatureToRaster's output is: " + str(Countries_Raster_Description.datasetType))
# Set Countries_Raster to be equal to 1 using Test Output as Land1_ElseNull
# Set local variables
TestinRaster = r"Temp\Countries_Raster.tif"
inWhereClause = "VALUE >= 1"

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
faults = "IndonesiaFaults_DGM95UTMz50S.shp"
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

# Create a directory to contain all viewsheds
print("Checking for Combine_Viewshed directory...")
if os.path.exists("Combine_Viewshed") is False:
    os.mkdir("Combine_Viewshed")
    print("The Combine_Viewshed directory was created successfully!")
else:
    print("The Combine_Viewshed directory was already created.")
Combine_Viewshed = "Combine_Viewshed"
print("The Combine_Viewshed directory is named " + str(Combine_Viewshed))

# Create a directory to contain all viewpoints
print("Checking for Combine_Viewpoints directory...")
if os.path.exists("Combine_Viewpoints") is False:
    os.mkdir("Combine_Viewpoints")
    print("The Combine_Viewpoints directory was created successfully!")
else:
    print("The Combine_Viewpoints directory was already created.")
Combine_Viewpoints = "Combine_Viewpoints"
print("The Combine_Viewpoints directory is named " + str(Combine_Viewpoints))

# Create a directory to contain all expanded viewsheds
print("Checking for expanded_viewsheds directory...")
if os.path.exists("expanded_viewsheds") is False:
    os.mkdir("expanded_viewsheds")
    print("The expanded_viewsheds directory was created successfully!")
else:
    print("The expanded_viewsheds directory was already created.")
expanded_viewsheds = "expanded_viewsheds"
print("The expanded_viewsheds directory is named " + str(expanded_viewsheds))

end_preperation_time = time.time()

# Begin Loop
############
start_viewpoints_and_viewshed_loop_time = time.time()

for iteration in range(3):
    # unique ID
    unique_id = iteration
    print("Start " + str(unique_id))
    # Create unique directories
    print("Checking for viewshed output directory...")
    if os.path.exists(f"Viewshed_{unique_id}") is False:
        os.mkdir(f"Viewshed_{unique_id}")
        print(f"The viewshed_{unique_id} output directory was created successfully!")
    else:
        print(f"The viewshed_{unique_id} output directory was already created.")
    # Run CreateRandomPoints
    print("CreateRandomPoints for " + str(unique_id))
    arcpy.management.CreateRandomPoints("Temp", "observationPoints.shp", r"Temp\multipart_oceanFaults.shp", "",
                                        25, "1000 Meter",
                                        "POINT", "")
    # Dissolve Random Points to a single multipart feature
    print("Dissolve for " + str(unique_id))
    arcpy.Dissolve_management(r"Temp\observationPoints.shp",
                              fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shp",
                              "", "", "MULTI_PART", "", "")
    # 2D Viewshed
    toolbox = arcpy.AddToolbox(r"2D_Viewshed_Analysis.tbx")
    # Set variables and run the 2D Script
    print("Create viewshed for " + str(unique_id))
    toolbox.Script(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shp", r"Temp\Land1_ElseNull.tif",
                   cellSize, f"Viewshed_{unique_id}")
    # rename viewshed out puts to allow them to be put into the raster calculator later. Must rename all four parts.
    ## rename viewshed_0.img to viewshed_{unique_id}.img
    os.rename(fr"Viewshed_{unique_id}\viewshed_0.img", fr"Viewshed_{unique_id}\viewshed_{unique_id}.img")
    print("The .img was successfully renamed from " + fr"Viewshed_{unique_id}\viewshed_0.img" + " to " +
          fr"Viewshed_{unique_id}\viewshed_{unique_id}.img")
    ## rename viewshed_0.img.aux.xml to viewshed_{unique_id}.img.aux.xml
    os.rename(fr"Viewshed_{unique_id}\viewshed_0.img.aux.xml", fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.aux.xml")
    print("The .img.aux.xml was successfully renamed from " + fr"Viewshed_{unique_id}\viewshed_0.img.aux.xml" + " to " +
          fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.aux.xml")
    ## rename viewshed_0.img.vat.dbf to viewshed_{unique_id}.img.vat.dbf
    os.rename(fr"Viewshed_{unique_id}\viewshed_0.img.vat.dbf", fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.dbf")
    print("The .img.vat.dbf was successfully renamed from " + fr"Viewshed_{unique_id}\viewshed_0.img.vat.dbf" + " to " +
          fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.dbf")
    ## rename viewshed_0.img.vat.cpg to viewshed_{unique_id}.img.vat.cpg
    os.rename(fr"Viewshed_{unique_id}\viewshed_0.img.vat.cpg", fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.cpg")
    print("The .img.vat.cpg was successfully renamed from " + fr"Viewshed_{unique_id}\viewshed_0.img.vat.cpg" + " to " +
          fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.cpg")
    # Move the renamed viewpoints and viewsheds to the Combined_Viewpoints and Combined_Viewshed directories.
    ## Move viewsheds
    ### Move .img
    shutil.move(fr"Viewshed_{unique_id}\viewshed_{unique_id}.img", fr"Combine_Viewshed\viewshed_{unique_id}.img")
    print(".img was moved from " + fr"Viewshed_{unique_id}\viewshed_{unique_id}.img" + " to "
          + fr"Combine_Viewshed\viewshed_{unique_id}.img" + " successfully!")
    ### Move .img.aux.xml
    shutil.move(fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.aux.xml", fr"Combine_Viewshed\viewshed_{unique_id}.img.aux.xml")
    print(".img.aux.xml was moved from " + fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.aux.xml" + " to "
          + fr"Combine_Viewshed\viewshed_{unique_id}.img.aux.xml" + " successfully!")
    ### Move .img.vat.dbf
    shutil.move(fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.dbf", fr"Combine_Viewshed\viewshed_{unique_id}.img.vat.dbf")
    print(".img.vat.dbf was moved from " + fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.dbf" + " to "
          + fr"Combine_Viewshed\viewshed_{unique_id}.img.vat.dbf" + " successfully!")
    ### Move .img.vat.cpg
    shutil.move(fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.cpg", fr"Combine_Viewshed\viewshed_{unique_id}.img.vat.cpg")
    print(".img.vat.cpg was moved from " + fr"Viewshed_{unique_id}\viewshed_{unique_id}.img.vat.cpg" + " to "
          + fr"Combine_Viewshed\viewshed_{unique_id}.img.vat.cpg" + " successfully!")
    ## Move viewpoints
    ### Move .cpg
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.cpg",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.cpg")
    print("Viewpoints .cpg was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.cpg" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.cpg" + " successfully!")
    ### Move .dbf
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.dbf",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.dbf")
    print("Viewpoints .dbf was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.dbf" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.dbf" + " successfully!")
    ### Move .prj
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.prj",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.prj")
    print("Viewpoints .prj was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.prj" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.prj" + " successfully!")
    ### Move .sbn
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.sbn",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.sbn")
    print("Viewpoints .sbn was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.sbn" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.sbn" + " successfully!")
    ### Move .sbx
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.sbx",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.sbx")
    print("Viewpoints .sbx was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.sbx" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.sbx" + " successfully!")
    ### Move .shp
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shp",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.shp")
    print("Viewpoints .shp was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shp" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.shp" + " successfully!")
    ### Move .shp.xml
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shp.xml",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.shp.xml")
    print("Viewpoints .shp.xml was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shp.xml" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.shp.xml" + " successfully!")
    ### Move .shx
    shutil.move(fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shx",
                fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.shx")
    print("Viewpoints .shx was moved from " + fr"Viewshed_{unique_id}\observationMultiPoints_{unique_id}.shx" + " to "
          + fr"Combine_Viewpoints\observationMultiPoints_{unique_id}.shx" + " successfully!")
    # Delete empty directories
    os.rmdir(f"Viewshed_{unique_id}")
    print("Removed the empty directory.")
    # expand all viewsheds
    outExpand = Expand(fr"Combine_Viewshed\viewshed_{unique_id}.img", 1, 1, "MORPHOLOGICAL")
    outExpand.save(rf"expanded_viewsheds\expanded_viewshed_{unique_id}.img")
############
# End of loop
arcpy.env.workspace = "expanded_viewsheds"
expanded_rasters = arcpy.ListRasters("", "IMG")
for raster in expanded_rasters:
    # list rasters
    raster_number = raster
    print("The expanded rasters are: " + raster)
    # find null cells and make binary
    outIsNull = IsNull(raster)
    print(outIsNull.save(f"binary_{raster_number}"))
binary_rasters = arcpy.ListRasters("binary_expanded_viewshed*", "IMG")
# Create binary_expanded_viewshed directory
print("Checking for binary_expanded_viewsheds directory...")
if os.path.exists("binary_expanded_viewsheds") is False:
    os.mkdir("binary_expanded_viewsheds")
    print("The binary_expanded_viewsheds directory was created successfully!")
else:
    print("The binary_expanded_viewsheds directory was already created.")
binary_expanded_viewsheds = "binary_expanded_viewsheds"
print("The binary_expanded_viewsheds directory is named " + str(binary_expanded_viewsheds))
for i in binary_rasters:
    # list rasters
    binary_raster_number = i
    print(f"binary_raster_{binary_raster_number}")
    binary_expanded = EqualTo(i, 0)
    print(binary_expanded.save(fr"binary_expanded_viewsheds\view1_{binary_raster_number}"))
# Combine the expanded viewsheds together using raster calculator
## Create list of prepared viewsheds
### Set workspace
arcpy.env.workspace = "binary_expanded_viewsheds"
### create list of rasters
rasters = arcpy.ListRasters(raster_type = "IMG")
### chack the list of rasters and check if it is a list
print("The type for rasters is: " + str(type(rasters)))
print("The rasters are: " + str(rasters))
### create an empty raster_objects list to populate later
raster_objects = []
### create a for loop that removes the first raster object, then adds the second to the removed, then the next iteration
### and on and on.
for raster in rasters:
    #### Create raster objects. These are data types that can be added together directly.
    a_raster_object = arcpy.sa.Raster(raster)
    #### append to the empty raster_objects list that you prior created
    raster_objects.append(raster_objects)
    print("INSIDE LOOP a_raster_object name and type: " + str(a_raster_object) + str(type(a_raster_object)))
    #### the method of "pop(integer) will take an object as specified by the integer from a list and "pop it out", in
    #### other words, it will remove the object and return it to you.
    #### This method will be used on raster_objects.
    #### Assign it a variable in order to call it many times in the loop. We are going to add all rasters to the popped raster.
    sum_raster_objects = raster_objects.pop(0)
    print("INSIDE LOOP sum_raster_objects is: " + str(sum_raster_objects) + str(type(sum_raster_objects)))
### check the loop!
print("AFTER LOOP a_raster_object name and type: " + str(a_raster_object) + str(type(a_raster_object)))
print("AFTER LOOP sum_raster_objects is: " + str(sum_raster_objects) + str(type(sum_raster_objects)))
### create a for loop that directly adds all of the raster objects together.
for object in raster_objects:
    print(object)
    sum_raster_objects = sum_raster_objects + object
# sum_raster_objects.save("combined_raster_nonbinary")
# print("sum_raster_objects is and is type of: " + str(sum_raster_objects) + str(type(sum_raster_objects)))



start_final_output_time = time.time()
end_viewpoints_and_viewshed_loop_time = time.time()

# Create a final viewshed output layer.

# Clean up directories

# run times
preperation_time = end_preperation_time - start_time
print("Data preperation took " + str(preperation_time) + " seconds to run.")
viewpoints_and_viewshed_loop_time = end_viewpoints_and_viewshed_loop_time - start_viewpoints_and_viewshed_loop_time
print("Viewpoints and viewsheds loop took " + str(viewpoints_and_viewshed_loop_time) + " seconds to run.")
end_time = time.time()
final_output_time = end_time - start_final_output_time
# print("Final output took " + str(final_output_time) + " seconds to run.")
# run_time = end_time - start_time
# print("It took " + str(run_time) + "seconds to run the script.")