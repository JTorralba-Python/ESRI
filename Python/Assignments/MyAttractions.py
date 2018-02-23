import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Cursors'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

fld1, fld2, fld3, fld4 = "NAME", "ADDR", "CITYNM", "ZIP"

cursor = arcpy.da.SearchCursor("MajorAttractions",(fld1,fld2,fld3,fld4))

for row in cursor:
    print "{}\n{}\n{}, CA {}\n\n".format(row[0],row[1],row[2],row[3])