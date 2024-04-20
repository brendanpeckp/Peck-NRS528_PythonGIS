
#####
# Step 0 - Practice tasks before we start.
#####
import arcpy

arcpy.env.workspace = r'C:\Peck_NRS528_PythonGIS\pythonProject\Classes\10_rasters\Step_0_Data'
workspace = arcpy.env.workspace
arcpy.env.overwriteOutput = True

in_features = r'RI_Forest_Health_Works_Project_Points_All_Invasives.shp'

# Task a: Run the buffer tool on Step_0_Data.zip/RI_Forest_Health_Works_Project_Points_All_Invasives.shp, with a
# distance of 1 mile:
buffered_feature = 'invasive_points_buffered.shp'

arcpy.analysis.Buffer(in_features, buffered_feature, '1 Miles', '', '', '', '', '')

# Task b: Dissolve your resulting buffer:
dissolved_feature = 'invasive_points_dissolved.shp'

arcpy.management.Dissolve(buffered_feature, dissolved_feature, '', '', 'MULTI_PART', '', '')

# Task c: On the original point file (RI_Forest_Health_Works_Project_Points_All_Invasives.shp), use a
# search cursor to print the "Owner" field within the attributes.
listFields = arcpy.ListFields(in_features)
fields = []
for field in listFields:
    # print(field.name)
    fields.append(field.name)
print("Input shapefile's list of field-names: " + str(fields))

field_owner_6 = []

with arcpy.da.SearchCursor(in_features, fields) as cursor:
    for row in cursor:
        if row[6] not in field_owner_6:
            field_owner_6.append(row[6])

print("There are " + str(len(field_owner_6)) + " record types in the 'owner' field. They are: " + str(field_owner_6))