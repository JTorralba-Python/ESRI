import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Cursors'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

fld1, fld2, fld3 = "NAME", "ESTAB", "EMP"

cur = arcpy.da.SearchCursor("MajorAttractions",(fld1,fld2,fld3))

for rec in cur:
    print "{} was established in {} and employs {} people".format(rec[0],rec[1],rec[2])