import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Cursors'
arcpy.env.workspace = os.path.join(wksp,"Corvallis.gdb")

arcpy.AddField_management("Parcel", "ACRES", "Double")

with arcpy.da.UpdateCursor("Parcel", ["SHAPE@AREA", "ACRES"]) as cursor:
    for rec in cursor:
        Area = rec[0]
        rec[1] = Area / 43560
        cursor.updateRow(rec)

print "Script completed."
