#####
# Step 3 - Executing multiple tools - and automating most of it
#####
import os.path

# We will use the exact same approach to generate a heatmap from a CSV file, but this time
# You will have to automate the extraction of start extent, opposite corner etc for the fishnet
# generation. I have given hints, but everything you are using here has been shown in last week's
# and this week's session.

# Using Step_3_Cepphus_grylle.csv:

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.

print("1. Convert the file to a shapefile.")
print(" ")

import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\05_scripts"

in_Table = os.path.join(r"Step_3_Cepphus_grylle.csv")
x_coords = "lon"
y_coords = "lat"
z_coords = ""
out_Layer = os.path.join("Cepphus_grylle_output_layer_ram") # saved in ram (ram will auto delete)
saved_Layer = os.path.join(r"Cepphus_grylle_output_layer_harddrive.shp") # saved on harddrive
# create arguements for the x, y event layer tool

spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
# Set the spatial reference

event_layer = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Print the total rows
print("Total Rows:")
print(arcpy.GetCount_management(out_Layer))

# Save to a layer file
arcpy.CopyFeatures_management(event_layer, saved_Layer)

saved_Layer_description = arcpy.Describe(saved_Layer).name
print("Saved layer name is: " + saved_Layer_description)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")

##### 2. Print the count of the number of records in the file. (Hint: see above!)
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-count.htm

print("Number of records on file:")
print(arcpy.management.GetCount(event_layer))

##### 3. Check the correct coordinate system has been applied (Hint: see last week!)
spatial_reference_description = arcpy.Describe(event_layer).spatialReference.name
print("Coordinate System: " + spatial_reference_description)

##### 4. Visualize the file in ArcPro by dragging it into the program.

print("Check VUI")

print(" ")
print("2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.")
print(" ")

extent_description = arcpy.Describe(event_layer).extent
print(extent_description)

print("Check VUI")

print(" ")
print("3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner")
print("using the extracted extent from above. Hint: Formatting of the coordinate is important when generating")
print('the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the')
print("entire thing is a string. Hint use: cellSizes of 0.25 degrees.")
print(" ")

outFeatureClass = "Step_3_Fishnet.shp"  # Name of output fishnet
print(outFeatureClass)
# name your fishnet. This will be a file written to the harddrive.

# Set the arguements. Now, a key part of this is coordinate format. This has to be written correctly in order to make it capable
# of taking in any extent.
originCoordinate = str(extent_description.XMin) + " " + str(extent_description.YMin) #-176.87 -51"  # Left bottom of our point data
yAxisCoordinate = str(extent_description.XMin) + " " + str(extent_description.YMax) # "-176.87 -41"  # This sets the orientation on the y-axis, so we head north
cellSizeWidth = "0.25"  # 10 degrees
cellSizeHeight = "0.25"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = ""  # Leave blank, as we have set cellSize
oppositeCorner = str(extent_description.XMax) + " " + str(extent_description.YMax) # "162.0200043 71.34999847"  # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE
# Set the origin of the fishnet

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)
# execute the fishnet tool

Fishnet_description = arcpy.Describe(event_layer)
print(Fishnet_description)

print("Fishnet created successfully!")
# I need to edit the fishnet tool so that originCoordinate, yAxisCoordinate and oppositeCorner are populated by
# my extracted extent.
## My exctracted extent: "-82 36.79312 -50.45 59.4333 NaN NaN NaN NaN"
## I must change originCoordinate, yAxisCoordinate and oppositeCorner from being hardwired to taking in the extracted
## extent automatically.
## I need to extract extent as a string and pull

print(" ")
print("4. Undertake a Spatial Join to join the fishnet to the observed points.")
print(" ")

target_features="Step_3_Fishnet.shp"
join_features="Cepphus_grylle_output_layer_harddrive.shp"
out_feature_class="Step_3_Cepphus_grylle_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""
# set arguments for the spatial join. As this was taken from step 2, make sure that you change the layer inputs and the output name.

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
# execute spatial join

Heat_Map_Description = arcpy.Describe(out_feature_class).name
print("Your output; " + Heat_Map_Description + " was created successfully!")
# Check if your output was created.

print("Check VUI")

print("")
print("5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:")
# arcpy.Delete_management()..
print("")
# What intermediates must I delete? I created 3 files, I want to delete the first two. Maybe in some cases I only want
# to delete the grid and keep the points layer.

if arcpy.Exists("Cepphus_grylle_output_layer_harddrive.shp"):
    arcpy.Delete_management("Cepphus_grylle_output_layer_harddrive.shp")
if arcpy.Exists("Step_3_Fishnet.shp"):
    arcpy.Delete_management("Step_3_Fishnet.shp")
# delete intermediate files.

if arcpy.Exists("Cepphus_grylle_output_layer_harddrive.shp"):
    print("Cepphus_grylle_output_layer_harddrive.shp still exists.")
else:
    print("Cepphus_grylle_output_layer_harddrive was deleted.")
if arcpy.Exists("Step_3_Fishnet.shp"):
    print("Step_3_Fishnet.shp still exists.")
else:
    print("Step_3_Fishnet.shp was deleted.")
# Check if it was deleted.

print(" ")
print("6. Visualize in ArcGIS Pro")
print(" ")
print("Check VUI")
# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# import arcpy
# arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# ArcGIS Pro or an other program such as Excel.

