# Step 0 - Warm up task

# Develop a small script that uses two datasets from RIGIS.org and undertake a geoprocessing routine on the
# data.

# This could be a spatial join, a buffer, an intersect, an extract by mask for example.
# there are no restrictions on the tool or dataset, and there is no answer file for this,
# so please do go forward with producing a simple script.

import os
import arcpy

arcpy.env.overwriteOutput = True

#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Classes\08_functions"
#######################################################################################################################

roads = os.path.join(r"step_0_data\TRANS_Roads_E911.shp")
description_roads = arcpy.Describe(roads)
print("The in-layer; " + str(description_roads.name) + " is a " + str(description_roads.dataType))
scenic_land = os.path.join(r"step_0_data\Scenic_Landscape_Inventory.shp")
description_scenic_land = arcpy.Describe(scenic_land)
print("The select-features; " + str(description_scenic_land.name) + " is a " + str(description_scenic_land.dataType))

selection = arcpy.management.SelectLayerByLocation(roads, "INTERSECT", scenic_land, "", "NEW_SELECTION", "")

scenic_roads = os.path.join(r"step_0_data\scenic_roads.shp")

arcpy.management.CopyFeatures(selection, scenic_roads, "", "", "", "")