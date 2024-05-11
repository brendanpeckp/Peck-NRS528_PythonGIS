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
    unique_id = directory # Unique id to give unique names to the outfiles as to not overwrite them
    directory_workspace = os.path.join(imagery_workspace, directory) # os.path.join to move the workspace into
    # appropriate directories as it iterates.
    arcpy.env.workspace = directory_workspace # execute the above line.
    rasters = arcpy.ListRasters()
    print(rasters)

    # For each iteration, the following script will be inside another directory. This will list rasters of the bands of
    # interest. These lists can be used later to do math with.
    raster_b4 = arcpy.Raster(arcpy.ListRasters("*b4*")[0])
    raster_b5 = arcpy.Raster(arcpy.ListRasters("*b5*")[0])

    # arcpy.Raster() allows pycharm to use the lists as raster objects. As raster objects, they may be put into
    # equations to be worked with on a cell to cell basis.
    nvdi = (raster_b5 - raster_b4) / (raster_b5 + raster_b4)
    nvdi_raster = arcpy.Raster(nvdi)
    print(nvdi_raster)
    nvdi_raster.save(f'ndvi_raster_{unique_id}.tif')




