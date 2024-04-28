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
import arcpy, os # arcpy for ListRasters and os for everything else
arcpy.CheckOutExtension("Spatial") # make sure that we have all the ability to work with rasters
arcpy.env.overwriteOutput = True # We want to overwrite the outputs
arcpy.env.workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_10" # The absolute workspace
defalt_workspace = arcpy.env.workspace # I can call the workspace later and change it

imagery_directories = os.listdir('imagery')
print(imagery_directories)

imagery_workspace = os.path.join(defalt_workspace, 'imagery')
print(imagery_workspace)

for directory in imagery_directories:
    unique_id = directory
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
    nvdi = (raster_b5 - raster_b4) / (raster_b5 + raster_b4)
    nvdi_raster = arcpy.Raster(nvdi)
    print(nvdi_raster)
    nvdi_raster.save(f'ndvi_raster_{unique_id}.tif')




