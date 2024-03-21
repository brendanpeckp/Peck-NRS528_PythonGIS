# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-03-10 22:22:32
Edited by Brendan Peck on : 2024-03-12
"""
#########
# Notes #
#########

#? Create a directory for intermediate data to be deleted later.
#? Give the user the option to comment out the intermidiate data should they want to keep it.
#? Use if keep_temp_files == False:
#?    arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))

#! check code by using the following.
#! print(whatever file inside)
#! if exists: print("______ ran successfully!")
#! desc.whatever attribute of whatever file
#! check run time
##! arcpy_start_time = time.time()
##! It subtracts the start time from the current time.
##! print('It took', time.time()-arcpy_start_time, 'seconds, to load arcpy.')
#! List dir - Use class 07, part 01.

#@ Remember that some tools will make on the fly data. If you want to use that data you will need to save it to a new file
#@ using
#@ arcpy.CopyFeatures_management(lyr, saved_Layer)
#@ if arcpy.Exists(saved_Layer):
#@    print("Created file successfully!")

#& Make sure all variables and files have simple, clear names that will remain descriptive of a DEM derivative for any
#& coastal area in the world.

#$ Have a dynamic workspace so that all calls back to the data remains true if code is sent to a new directory with data
#$ for a different study area. Use os.join.something(whateverdata)
#$ Use os.path.join(directory, "whateverFile")

################
# END OF NOTES #
################

###################
# Start of Script #
###################

#
## Setup ##
### The setup has 6 parts.
#### Import system modules
#### Set environment
#### Use arcpy.env.overwriteOutput = True
#### Include licences
#### Make a temp directory to be deleted later.
#### Check your work
#
import time
print("START SETUP")
start_setup_time = time.time()
print("START IMPORTS")

import arcpy
from arcpy.ia import *
from arcpy.ia import *
from arcpy.ia import *
from arcpy.sa import *
import os

print("FINISHED IMPORTS")

#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Midterm\Workspace"
#######################################################################################################################
arcpy.env.workspace = workspace
print("The input data is composed of " + str(len(arcpy.ListFiles("*"))) + " files.")
print("The workspace includes two files as input data. Those are: " + str(arcpy.ListFiles("*")))

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# The Below are licences. They don't actually run anything here.
# Check out any necessary licenses.
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

# Create a temporary directory to be deleted later.
print("Checking for temporary directory...")
if os.path.exists("Temp") is False:
    os.mkdir("Temp")
    print("The temporary directory was created successfully!")
else:
    print("The temporary directory was already created.")
Temporary_Directory = os.path.join("Temp")
print("The temporary directory is named " + str(os.path.join(Temporary_Directory)))

#
## Set Null Process ##
### This process includes 3 parts:
#### Set Local Variables
#### Execute Set Null
#### Save Output
#

#
#### Set Local Variables ####
#

print("FINISHED WITH SETUP")
end_setup_time = time.time()
elapsed_setup_time = end_setup_time - start_setup_time
print("Setup process took " + str(elapsed_setup_time) + " seconds to run")

print("START DATA PROCESSING")
start_dataProcessing_time = time.time()

print("START 1st SET NULL")

inDEM_Raster = os.path.join("ProjectedAndClipped_VoidFilledSRTM_DEM_3ArcSecond.tif")
inFalseRaster = 1
whereClause = "VALUE >= 1"
# Check the local variables.
print("The input DEM is " + str(inDEM_Raster))
print("The inFalseRaster is " + str(inFalseRaster))
print("The whereClause is " + str(whereClause))

#
#### Execute Set Null
#
SeaLevel1 = SetNull(inDEM_Raster, inFalseRaster, whereClause)
print("The output for SetNull is " + str(SeaLevel1))

#
#### Save Output
#
SeaLevel1.save(os.path.join(r"Temp\SetNull_Project1.tif"))
print("The saved output file for SetNull is " + str(SeaLevel1))

print("FINISHED 1st SET NULL")

print("START REGION GROUP")

#
## Region Group Process ##
### This process includes 3 parts:
#### Set variables
#### Execute RegionGroup
#### Save output
#

#
#### Set variables
#
inSeaLevelRaster = os.path.join(r"Temp\SetNull_Project1.tif")

#
#### Execute RegionGroup
#
SeaLevelGroups = RegionGroup(inSeaLevelRaster, "FOUR", "WITHIN", "ADD_LINK")
print("The output for RegionGroup is " + str(SeaLevelGroups))

#
#### Save output
#
SeaLevelGroups.save(os.path.join(r"Temp\RegionG_SetNull1.tif"))
print("The saved output for RegionGroup is " + str(SeaLevelGroups))

print("FINISHED REGION GROUP")

print("START TEST")

#
## Test Process ##
### This process includes 3 parts:
#### Set variables
#### Execute Test
#### Save output
#

#
#### Set variables
#
inGroupedRaster = os.path.join(r"Temp\RegionG_SetNull1.tif")
inWhereClause = "COUNT >= 50"

#
#### Execute Test
#
Ocean1_else0 = Test(inGroupedRaster, inWhereClause)
print("The output for Test is " + str(Ocean1_else0))

#
#### Save output
#
Ocean1_else0.save(os.path.join(r"Temp\Test_RegionG_Se1.tif"))
print("The saved output for Test is " + str(Ocean1_else0))

print("FINISHED TEST")

print("START 2nd SET NULL")

#
## 2nd Set Null Process ##
### This process includes 3 parts:
#### Set Local Variables
#### Execute Set Null
#### Save Output
#

#
#### Set Local Variables
#
in_Ocean1_else0_Raster = os.path.join("ProjectedAndClipped_VoidFilledSRTM_DEM_3ArcSecond.tif")
inFalseRaster_2 = 1
whereClause_2 = "VALUE = 0"

#
#### Execute Set Null
#
Ocean1 = SetNull(in_Ocean1_else0_Raster, inFalseRaster_2, whereClause_2)
print("The output for the 2nd SetNull is " + str(Ocean1))

#
#### Save Output
#
Ocean1.save(os.path.join(r"Workspace\OceanMaskRaster.tif"))

print("FINISHED 2nd SET NULL")

print("FINISHED WITH DATA PROCESSING")
end_dataProcessing_time = time.time()
elapsed_dataProcessing_time = end_dataProcessing_time - start_dataProcessing_time
print("Data processing took " + str(elapsed_dataProcessing_time) + " seconds to run.")

############
# Clean up #
############
arcpy.Delete_management(os.path.join(Temporary_Directory))
arcpy.Delete_management(os.path.join(Temporary_Directory, "RegionG_SetNull1.tif"))
arcpy.Delete_management(os.path.join(Temporary_Directory, "SetNull_Project1.tif"))
arcpy.Delete_management(os.path.join(Temporary_Directory, "Test_RegionG_Se1.tif"))
arcpy.Delete_management(os.path.join(Temporary_Directory))

print("The final output is " + str(Ocean1))
