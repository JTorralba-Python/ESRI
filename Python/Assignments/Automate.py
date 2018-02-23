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

fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    print fc

print "******************************"

fds = arcpy.ListDatasets()
for fd in fcs:
    print fd
    fcs = arcpy.ListFeatureClasses("","",fd)
    for fc in fcs:
        print "\t" + fc

print "script completed"

