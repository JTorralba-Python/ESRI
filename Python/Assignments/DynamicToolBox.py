import arcpy
import os

arcpy.env.overwriteOutput = True
wksp = arcpy.env.workspace = r'E:\Student\PYTH\Sharing_scripts'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

arcpy.AddMessage("Message")
arcpy.AddWarning("Warning")
arcpy.AddError("Error")
arcpy.AddMessage("Message")

print "Script completed."
