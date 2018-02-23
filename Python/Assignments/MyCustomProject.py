import arcpy

arcpy.env.workspace = r"E:/Student/PYTH/Sharing_scripts/Corvallis.gdb"
arcpy.env.overwriteOutput = True

distance = arcpy.GetParameterAsText(0)
output_FC = arcpy.GetParameterAsText(1)

sql = """ "PARK_NAME" = 'Central Park' """

arcpy.MakeFeatureLayer_management("Parks", "CentralPark", sql)
arcpy.MakeFeatureLayer_management("ParkingMeters", "Meters")

arcpy.SelectLayerByLocation_management("Meters", "WITHIN_A_DISTANCE",
                                       "CentralPark", distance,
                                       "NEW_SELECTION")

with arcpy.da.UpdateCursor("Meters", ["FLAG"]) as cursor:
    for row in cursor:
        row[0] = "Y"
        cursor.updateRow(row)

arcpy.CopyFeatures_management("Meters", output_FC)

count = arcpy.GetCount_management(output_FC)
print "Number of meters to program: {0}".format(count)

print "Script completed."
