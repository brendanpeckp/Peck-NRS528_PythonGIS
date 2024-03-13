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

import arcpy
from arcpy.ia import *
from arcpy.ia import *
from arcpy.ia import *
from arcpy.sa import *
import os
import time


#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Midterm\Workspace"
#######################################################################################################################
arcpy.env.workspace = workspace
print("The input data is composed of " + str(len(arcpy.ListFiles("*"))) + " files.")
print("Those files are: " + str(arcpy.ListFiles("*")))

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# The Below are licences. They don't actually run anything here.
# Check out any necessary licenses.
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

# Here is the input DEM. The tool was designed for 3-arc-second void-filled SRTM data that has been clipped and
# projected to the user's study area.
InputPreparedDEM = arcpy.Raster(os.path.join("ProjectedAndClipped_VoidFilledSRTM_DEM_3ArcSecond.tif"))
print("The input DEM is named: " + str(InputPreparedDEM))
print(arcpy.Describe.datasetType(arcpy.os.path.join("ProjectedAndClipped_VoidFilledSRTM_DEM_3ArcSecond.tif")))

Input_false_raster_or_constant_value = 1
Input_false_raster_or_constant_value_2_ = 1

# # Process: Set Null (Set Null) (ia)
# SeaLevel1_elseNULL = "C:\\GeoData\\ArcProProjectFiles\\DEM_FloodTool_PythonTemplate\\DEM_FloodTool_PythonTemplate.gdb\\SeaLevel1_elseNULL"
# Set_Null = SeaLevel1_elseNULL
# SeaLevel1_elseNULL = arcpy.ia.SetNull(SRTMvoidfilled_YardlandIrelandFlood, Input_false_raster_or_constant_value, "VALUE >= 1")
# SeaLevel1_elseNULL.save(Set_Null)

# # Process: Region Group (Region Group) (sa)
# SeaLevelGroups = "C:\\GeoData\\ArcProProjectFiles\\DEM_FloodTool_PythonTemplate\\DEM_FloodTool_PythonTemplate.gdb\\SeaLevelGroups"
# Region_Group = SeaLevelGroups
# SeaLevelGroups = arcpy.sa.RegionGroup(SeaLevel1_elseNULL, "FOUR", "WITHIN", "ADD_LINK", None)
# SeaLevelGroups.save(Region_Group)
#
#
# # Process: Test (2) (Test) (ia)
# Ocean1_else0 = "C:\\GeoData\\ArcProProjectFiles\\DEM_FloodTool_PythonTemplate\\DEM_FloodTool_PythonTemplate.gdb\\Ocean1_else0"
# Test_2_ = Ocean1_else0
# Ocean1_else0 = arcpy.ia.Test(SeaLevelGroups, "Count >= 50")
# Ocean1_else0.save(Test_2_)
#
#
# # Process: Set Null (2) (Set Null) (ia)
# Ocean1 = "C:\\GeoData\\ArcProProjectFiles\\DEM_FloodTool_PythonTemplate\\DEM_FloodTool_PythonTemplate.gdb\\Ocean1"
# Set_Null_2_ = Ocean1
# Ocean1 = arcpy.ia.SetNull(Ocean1_else0, Input_false_raster_or_constant_value_2_, "VALUE = 0")
# Ocean1.save(Set_Null_2_)