
#####
# Step 3 - Executing a tool
#####

# Part a - Buffer_analysis

# Help on Tool: http://desktop.arcgis.com/en/arcmap/10.3/tools/analysis-toolbox/buffer.htm
# we definitely should refer to this when we are working with the tool, as it provides detail
# about the tool.

import arcpy

# The tool syntax looks something like this (I put a break in there to fit on page, will still work):
# Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field,
#                 {line_side}, {line_end_type}, {dissolve_option}, {dissolve_field}, {method})
# Optional commands are shown by squiggly brackets {}.

# Here is an example buffer analysis broken out into variables, roads does not exist:
# in_features = r"C:\Data\Course_ArcGIS_Python\Classes\04_arcpy\DataFolder_Step_3_data\Roads.shp"
# out_feature_class = r"C:\Data\Course_ArcGIS_Python\Classes\04_arcpy\DataFolder_Step_3_data\Roads_Buffer.shp"
# buffer_distance_or_field = "1 meter"
# line_side = "#"
# line_end_type = "#"
# dissolve_option = "#"
# dissolve_field = "#"
# method = "#"
# arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)

# Tasks - Using the files provided in Step_3_data.zip, under take the following:
##### 1. Execute the Buffer tool on Places_Been.shp, with a buffer of 100 meters, you will probably need to use method = GEODESIC

# import arcpy
# in_features = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\Places_Been.shp"
# out_feature_class = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\Places_Been_buffered.shp"
# buffer_distance_or_field = "100 meter"
# line_side = "#"
# line_end_type = "#"
# dissolve_option = "#"
# dissolve_field = "#"
# method = "GEODESIC"
# arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)

##### 2. Execute the Buffer tool on URI_Campus_Roads_OSM.shp twice, first with a buffer of 100 meters (everything else as default).
##### On the second run, set line_side to "RIGHT", and line_end_type to "FLAT". Compare the differences in the GIS.

# 1st run: 100 meter buffer on URI_Campus_Roads_OSM.shp
import arcpy
in_features = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\URI_Campus_Roads_OSM.shp"
out_feature_class = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\output_data\URI_Campus_Roads_OSM_buffered100.shp"
buffer_distance_or_field = "100 meter"
line_side = "#"
line_end_type = "#"
dissolve_option = "#"
dissolve_field = "#"
method = "GEODESIC"
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)

# 2nd run: 100 meter buffer on URI_Campus_Roads_OSM.shp with line side as right and line end type as flat.
in_features = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\URI_Campus_Roads_OSM.shp"
out_feature_class = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\output_data\URI_Campus_Roads_OSM_buffered100RIGHTFLAT.shp"
buffer_distance_or_field = "100 meter"
line_side = "RIGHT"
line_end_type = "FLAT"
dissolve_option = "#"
dissolve_field = "#"
method = "GEODESIC"
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)