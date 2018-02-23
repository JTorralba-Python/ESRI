import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Cursors'
arcpy.env.workspace = os.path.join(wksp,"Corvallis.gdb")

rows = [["Benton", (-123.40,44.49)],["Linn", (-122.49,44.48)],["Polk", (-123.38,44.89)],["Tillamook", (-123.65,45.45)]]

arcpy.CreateFeatureclass_management(arcpy.env.workspace, "CountyPNT", "Point")

arcpy.AddField_management("CountyPNT", "NAME", "TEXT")

cursor = arcpy.da.InsertCursor("CountyPNT", ["NAME", "SHAPE@XY"])

for row in rows:
    print row
    cursor.insertRow(row)

del cursor

print "Script completed."
