#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Student
#
# Created:     30/09/2015
# Copyright:   (c) Student 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy

arcpy.env.workspace = r'E:\Student\PYTH\Describing_Data\Corvallis.gdb'

desc = arcpy.Describe("Schools")
#print "dataType\t\t" + dsc.dataType
#print "shapeType\t\t" + dsc.shapeType

#sr = dsc.spatialReference
#print "SR name\t\t\t" + sr.name
#print "SR GCS\t\t\t" +sr.GCS.name

print "Name: {} Shape: {} Type: {}".format(desc.name, desc.shapeType,desc.datasetType)

for fld in desc.fields:
    print "\t{}".format(fld.name)

descGDB = arcpy.Describe(arcpy.env.workspace)
print "GDB Type: {} Release {} Path {}".format(descGDB.workspaceType,descGDB.release,descGDB.path)

