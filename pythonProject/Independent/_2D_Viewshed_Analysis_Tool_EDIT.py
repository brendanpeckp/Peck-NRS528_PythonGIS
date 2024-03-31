
import arcpy, os, sys, time


##obs_features = r"C:\Users\jason.EDC\OneDrive - University of Rhode Island\Papers\Viewshed_analysis\Viewshed_tool\_2D_viewshed_tool_ArcPro\Sample_data\obs_feature.shp"
##LOS_barriers = r"C:\Users\jason.EDC\OneDrive - University of Rhode Island\Papers\Viewshed_analysis\Viewshed_tool\_2D_viewshed_tool_ArcPro\Sample_data\LOS_barrier.img"  # barrier = 1, other = Nodata
##outWS = r"C:\Temp"
##cellsize = 2

obs_features = os.path.join("observationFeatures.shp")
LOS_barriers = os.path.join("Land1_ElseNull.tif")  # barrier = 1, other = Nodata
cellsize = 50000
outWS = os.path.join("Temp")


Temp = os.path.join("Temp")
if not os.path.exists(Temp):
    os.makedirs(Temp)

arcpy.env.workspace = Temp
arcpy.env.scratchWorkspace = Temp
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = LOS_barriers

# Get object ID field name                                
OID_field = arcpy.Describe(obs_features).oidfieldname  

# For each feature in obs_features
rows = arcpy.da.SearchCursor(obs_features, [OID_field])
for row in rows:

    sT1 = time.perf_counter()
    
    # Get current target feature
    ID = row[0]
    arcpy.env.extent = ""
##    select_feature = r"%s\select_feature_.shp" % tempWS
    arcpy.Select_analysis(obs_features, "select_feature.shp", "%s = %s" % (OID_field, ID))

    arcpy.env.extent = LOS_barriers   


    # Calculate distances from target feature...
    print("select_feature.shp")
    print(cellsize)
    print(LOS_barriers)
    dst_w_barriers = arcpy.sa.EucDistance("select_feature.shp", cell_size = cellsize, in_barrier_data = LOS_barriers)  # distance around barriers
    dst_no_barriers = arcpy.sa.EucDistance("select_feature.shp", cell_size = cellsize)    # Euclidean distance


    # Calculate correction factor to reduce errors in shortest path distance
    maxD = float(arcpy.GetRasterProperties_management(dst_no_barriers, "MAXIMUM")[0])
    dummy_barrier = arcpy.sa.SetNull(dst_no_barriers, 1, "Value < %s" % maxD)    # null raster with a small number of real pixels outside max viewshed distance. Needed to force EucDist tool to calculate distances in "barrier" mode
    dst_w_dummy_barriers = arcpy.sa.EucDistance("select_feature.shp", cell_size = cellsize, in_barrier_data = dummy_barrier)
    diff_cor = dst_w_dummy_barriers-dst_no_barriers   # difference between distance calculated in Euclidean vs shortest path distance mode    


    # Calculate difference between Shortest Path and Euclidean distances and apply correction
    diff = dst_w_barriers - dst_no_barriers - diff_cor
##    diff.save(r"%s\diff.img" % tempWS)

    # Classify 2D viewshed: distances < 0.9 are in viewshed
    _2D_viewshed_binary = arcpy.sa.Test(diff, "Value < 0.9")
    _2D_viewshed = arcpy.sa.SetNull(_2D_viewshed_binary, 1, "Value = 0")
    _2D_viewshed.save(r"%s\viewshed_%s.img" % (outWS, ID))


    # Calculate processing time for 2D viewshed method
    proc_time = round((time.perf_counter()-sT1), 0)
    print ("%s completed in %s seconds" % (ID, round(proc_time, 0)))
    arcpy.AddMessage("%s completed in %s seconds" % (ID, round(proc_time, 0)))

del rows, row
