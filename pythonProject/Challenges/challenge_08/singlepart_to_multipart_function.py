import os, arcpy
arcpy.env.overwriteOutput = True
#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_08"
#######################################################################################################################
arcpy.env.workspace = workspace

def singlepart_to_multipart(in_features): # Declares the name of the function.
    '''This function takes singlepart line shapefiles and uses the ESRI Dissolve tool to convert it to a single
    multipart feature. It also describes the input and out put data.'''
    # describe_in_features = arcpy.Describe(os.path.join("gem_active_faults_harmonized.shp"))
    describe_in_features = arcpy.Describe(in_features) # Declare description of input data to be used later.
    print("The input data, " + str(describe_in_features.name) + " is a " + str(describe_in_features.dataType)) # This describes the input data
    print("The input shape type is a " + str(describe_in_features.shapeType))

    if not os.path.exists(os.path.join("OutputData")): # This will check for an output directory and make one if needed.
        os.mkdir(os.path.join("OutputData"))
        print("OutputData folder was created successfully.")
    else:
        print("OutputData folder already exists.")

    out_feature_class = os.path.join(r"OutputData\multipart_line.shp") # Declares the name of the ouput data. It goes into the output directory.
    arcpy.management.Dissolve(in_features, out_feature_class, "", "", "MULTI_PART", "", "") # Runs the ArcPro tool; Dissolve.
    describe_out_feature_class = arcpy.Describe(out_feature_class) # Declares description name.
    print("The output data, " + str(describe_out_feature_class.name) + " is a " + str(describe_out_feature_class.dataType)) # Describes output data.
    print("The output shape type is " + str(describe_out_feature_class.shapeType))

# This line uses the function to dissolve the active fault database.
# singlepart_to_multipart(os.path.join(r"InputData_1_SeismicFaults\gem_active_faults_harmonized.shp"))

# This line will do tha same as the last, but with RI roads from RIGIS. It will replace the previous output.
singlepart_to_multipart(os.path.join(r"InputData_2_RoadsRI\TRANS_Roads_E911.shp"))

in_features = os.path.join(r"OutputData\multipart_line.shp")
out_feature_roadsideArea = os.path.join(r"OutputData\roadsideArea.shp")
arcpy.analysis.Buffer(in_features, out_feature_roadsideArea, "100 Feet", "FULL", "ROUND", "", "")