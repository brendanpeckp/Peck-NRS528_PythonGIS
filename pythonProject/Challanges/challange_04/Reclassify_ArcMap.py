######
## Notes
######

## I want to use the Reclassify tool to change the National Land Cover Dataset' pixel values from origanal to three classes
## I only want classes of forest, developed, and other.

## The input data is called NLCD_2016.img

## Refer to https://desktop.arcgis.com/en/arcmap/10.5/tools/spatial-analyst-toolbox/reclassify.htm#S_GUID-5FF3BD2A-DB58-4833-88C5-CB44FDD59E77
## to learn about the reclassify tool.

######
## Work
######

## Import arcpy to access tools.
import arcpy

## Assess previous import time
### Import time
import time
### Setting this variable is like doing "Total = 0" It creates a start to compare to later.
### In this case it records current time. Later that will be used to calculate elapsed time.
arcpy_start_time = time.time()
### A print statement.
### It subtracts the start time from the current time.
print('It took', time.time()-arcpy_start_time, 'seconds, to load arcpy.')

## Execute Reclassify
### Here is an example from Step_3.py to refer from.
#### import arcpy
#### in_features = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\URI_Campus_Roads_OSM.shp"
#### out_feature_class = r"C:\Peck-NRS528_PythonGIS\pythonProject\Classes\04_arcpy\Step_3_data\output_data\URI_Campus_Roads_OSM_buffered100.shp"
#### buffer_distance_or_field = "100 meter"
#### line_side = "#"
#### line_end_type = "#"
#### dissolve_option = "#"
#### dissolve_field = "#"
#### method = "GEODESIC"
#### arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)

### I notice that the parameters match the order of the documentation. So, I will just copy and paste each parameter from
### the documentation and edit it.

### The input data
in_raster = r"NLCD_2016.img"
print(in_raster)

### A location to put the output
out_raster = r"C:\Peck-NRS528_PythonGIS\pythonProject\Challanges\challange_04\output_data\NLCD_2016_reclassed.img"
print(out_raster)
#### For some reason my output data did not go to this above path. It's not a problem, but its not perfect. 

### Select a field to reclassify
reclass_field = "Value"
print(reclass_field)

### import other modules because RemapValue is not supported.
from arcpy import env
from arcpy.sa import *

### Choose values and change them.
remap = RemapValue([[11,0],[21,1],[22,1],[23,1],[24,1],[31,0],[41,2],[42,2],[43,2],[52,0],[71,0],[81,1],[82,1],[90,2],[95,0],["NODATA","NODATA"]])
print(remap)

### EXECUTE!
#### The Reclassify command takes the input data, finds the field to edit, and the edits choosen, then makes a new file
#### that has been edited.
outReclassify = Reclassify(in_raster, reclass_field, remap)
print(outReclassify)