import os, arcpy
arcpy.env.overwriteOutput = True
#######################################################################################################################
# USERS: CHANGE YOUR WORKSPACE FILEPATH BETWEEN THE QUOTATION MARKS.
workspace = r"C:\Peck_NRS528_PythonGIS\pythonProject\Challenges\challenge_08"
#######################################################################################################################
arcpy.env.workspace = workspace

def singlepart_to_multipart(in_features):
    '''This function takes singlepart line shapefiles and uses the ESRI Dissolve tool to convert it to a single
    multipart feature. It also describes the input and out put data.'''
    describe_in_features = arcpy.Describe(os.path.join("gem_active_faults_harmonized.shp"))
    print("The input data, " + str(describe_in_features.name) + " is a " + str(describe_in_features.dataType))
    out_feature_class = os.path.join("faults_dissolved.shp")
    arcpy.management.Dissolve(in_features, out_feature_class, "", "", "MULTI_PART", "", "")
    describe_out_feature_class = arcpy.Describe(os.path.join("faults_dissolved"))
    print("The output data, " + str(describe_out_feature_class.name) + " is a " + str(describe_out_feature_class.dataType))

# in_features = os.path.join("gem_active_faults_harmonized.shp")
# singlepart_to_multipart(in_features)

singlepart_to_multipart(os.path.join("gem_active_faults_harmonized.shp"))