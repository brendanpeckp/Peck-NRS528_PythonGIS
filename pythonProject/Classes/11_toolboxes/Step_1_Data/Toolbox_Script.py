import arcpy
import sys

input_1 = sys.argv[1]
input_2 = sys.argv[2]

argument_list = [input_1, input_2]

for i in argument_list:
    arcpy.AddMessage("Argument = " + str(i))
