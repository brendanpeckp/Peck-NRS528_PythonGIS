import arcpy
import sys

input_file = sys.argv[1]

desc = arcpy.Describe(input_file)

arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
arcpy.AddMessage("Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
arcpy.AddMessage("Coordinate System name =" + str(desc.spatialReference.name))
arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))