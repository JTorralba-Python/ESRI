sql = "ESTAB > 0 AND ESTAB < 1956"
fi = arcpy.FieldInfo()
fi.addField("ESTAB","Established","","")
fi.addField("ACRES","","HIDDEN","")
arcpy.MakeFeatureLayer_management("MajorAttractions","MA","","",fi)
arcpy.SelectLayerByAttribute_management("MA","NEW_SELECTION",sql)

