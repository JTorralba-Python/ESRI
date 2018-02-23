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

fc_list = arcpy.ListFeatureClasses()
for name in fc_list:
    desc = arcpy.Describe(name)
    featCount = arcpy.GetCount_management(name)
    print "Name: {} Shape: {} SR: {} Count: {}".format(desc.name,desc.shapeType,desc.spatialReference.name,featCount)

print "script completed"

