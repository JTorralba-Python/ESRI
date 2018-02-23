import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Cursors'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

sql = "ESTAB = 9999"

with arcpy.da.UpdateCursor("MajorAttractions",("NAME","ESTAB"),sql) as cursor:
    for rec in cursor:
        print "Updating features {}".format(rec[0])
        rec[1] = 0
        print rec[1]
        cursor.updateRow(rec)

