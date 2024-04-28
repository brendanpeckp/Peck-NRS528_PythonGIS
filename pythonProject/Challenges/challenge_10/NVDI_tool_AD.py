# This tool takes Landsat-8 imagery and outputs NVDI.
# About the data:
## The data is in raster format.
## The data is made of 12 bands. The tool only needs bands 4 and 5.
## The data is for several months. All images cover the same geographic area.
## Each month is stored in a seperate directory.

# Script explanation:
## Create a final output directory
## Loop through directories
    ## create a NVDI image by subtracting 4 from five
    ## save the created NVDI to the final output directory

# Overview of possible tools:
## arcpy.CheckOutExtension("Spatial") This may be useful to make sure arcpy works correctly
## arcpy.ListRasters() This will create a list of rasters inside of a directory.
## Step 2 from class goes over numpy. It may be more direct for subtraction of cell values. (rather than Raster Calculator)

# SETUP
import arcpy, os
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_10"
defalt_workspace = arcpy.env.workspace

# create final output directory

#### AD - you should use a not exists here.
if not os.path.exists('NVDI_Directory'):
    print("NVDI_Directory created successfully!")
else:
    os.makedirs('NVDI_Directory')

imagery_directories = os.listdir('imagery')
print(imagery_directories)

#### AD - Always use os.path.join for easier folder handling
imagery_workspace = os.path.join(defalt_workspace, "imagery")
print(imagery_workspace)

for directory in imagery_directories:
    #### AD - os.path.join again
    directory_workspace = os.path.join(imagery_workspace, directory)
    arcpy.env.workspace = directory_workspace
    rasters = arcpy.ListRasters()
    print(rasters)

    #### AD - Here's how I would find B4 and B5 file, listrasters returns a list, hence [0], I am assuming
    #### only one file called b4 in there.
    raster_b4 = arcpy.Raster(arcpy.ListRasters("*b4*")[0])
    raster_b5 = arcpy.Raster(arcpy.ListRasters("*b5*")[0])

    #### AD - by converting b4/b5 to an arcpy.Raster object, I can do math on it, without using rastercalculator.
    nvdi = raster_b4 + raster_b5


# # first write a code to take NVDI for one month
# arcpy.env.workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_10\201502"
#
# band_list = arcpy.ListRasters()
# print(band_list)
#
# band_list = band_list[5:7]
# print(band_list)
#
# print(band_list[0])
# print(band_list[1])
#
# inBand4 = arcpy.Raster(band_list[0])
# lowerLeft = arcpy.Point(inBand4.extent.XMin,inBand4.extent.YMin)
# cellSize = inBand4.meanCellWidth
# array4 = arcpy.RasterToNumPyArray(inBand4, nodata_to_value=0)
#
# print(array4.shape)
#
# newRaster = arcpy.NumPyArrayToRaster(array4, lowerLeft, cellSize, value_to_nodata=0)
# newRaster.save("test.tif")