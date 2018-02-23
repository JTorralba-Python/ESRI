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

arcpy.env.workspace = r'E:\Student\PYTH\Describing_Data\Tahoe\All'

desc = arcpy.Describe("E:\Student\PYTH\Describing_data\Tahoe\Emer\erelev")
rasExtent = desc.extent

ras_list = arcpy.ListRasters()

for name in ras_list:
    arcpy.Clip_management(name, str(rasExtent),'{}_clip'.format(name))

print "script completed"

