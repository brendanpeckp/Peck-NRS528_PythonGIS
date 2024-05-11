import arcpy
from arcpy import ddd
from arcpy.sa import *

# Set the current workspace
arcpy.env.workspace = 'C:\Peck_NRS528_PythonGIS\pythonProject\Final_Toolbox'
workspace = arcpy.env.workspace
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("spatial")

# Get and print a list of TIFs from the workspace
inBathy = []
rasters = arcpy.ListRasters("*", "TIF")
for raster in rasters:
    print(raster)
    inBathy.append(raster)
print(inBathy)

# Process: Mosaic To New Raster (Mosaic To New Raster) (management)
mosaic = arcpy.management.MosaicToNewRaster(inBathy, workspace, 'mosaicBathy.img', '', '32_BIT_SIGNED', '', 1, 'LAST', '')
mosaic = arcpy.Raster(mosaic)
print(mosaic)

# Process: Slope (Slope) (3d)
slope = arcpy.ddd.Slope('mosaicBathy.img', 'slope.img', 'DEGREE', 1,
                'PLANAR', 'METER', 'GPU_THEN_CPU')
slope = arcpy.Raster(slope)
print(slope)

# Process: Reclassify (Reclassify) (3d)
remap = RemapRange([[0, 22.5, 1], [22.5, 45, 2], [45, 90, 0]])
reclassify = arcpy.sa.Reclassify('slope.img', 'VALUE', remap, 'NODATA')
reclassify = arcpy.Raster(reclassify)
reclassify.save('bathyGradeClasses.img')
print(reclassify)