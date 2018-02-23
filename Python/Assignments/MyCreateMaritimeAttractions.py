import arcpy
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Selections'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

newField1 = arcpy.AddFieldDelimiters(arcpy.env.workspace, "TYPE")
newField2 = arcpy.AddFieldDelimiters(arcpy.env.workspace, "ESTAB")

maritimeSQLExp = newField1 + " = " + "'Maritime'"
historicSQLExp = newField2 + " > 0 and " + newField2 + " < 1956"

arcpy.MakeFeatureLayer_management("Climate","MaritimeLyr",maritimeSQLExp)
arcpy.MakeFeatureLayer_management("MajorAttractions","HistoricLyr",historicSQLExp)

arcpy.SelectLayerByLocation_management("HistoricLyr","COMPLETELY_WITHIN","MaritimeLyr","","NEW_SELECTION")

featCount = arcpy.GetCount_management("HistoricLyr")
print featCount

arcpy.CopyFeatures_management("HistoricLyr","MaritimeAttractions")
arcpy.MakeFeatureLayer_management("MaritimeAttractions","MA")
arcpy.Delete_management("MaritimeLyr")
arcpy.Delete_management("HistoricLyr")
