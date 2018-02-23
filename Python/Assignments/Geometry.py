import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Geometry_objects'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

#pnt = arcpy.Point(6285430.0, 1844965.66)

#with arcpy.da.UpdateCursor("MajorAttractions", ("SHAPE@XY"), "NAME = 'BALBOA PARK'") as cur:
#    for rec in cur:
#        rec[0] = pnt
#        cur.updateRow

g = arcpy.Geometry()
geomList = arcpy.CopyFeatures_management("Freeways",g)
length = 0
i = 0
for geom in geomList:
    length = length + geom.length
    i = i + 1

print "{} recods = length of {}".format(i,length)



print "Script completed."
