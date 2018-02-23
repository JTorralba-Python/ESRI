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
import os

wksp = arcpy.env.workspace = r'E:\Student\PYTH\Automating_scripts'
arcpy.env.workspace = os.path.join(wksp,"SanDiego.gdb")

fc_list = arcpy.ListFeatureClasses()

for featClass in fc_list:
    desc = arcpy.Describe(featClass)
    if desc.shapeType == 'Point':
        buffDist = '1000 feet'
    elif desc.shapeType == 'Polyline':
        buffDist = '500 feet'
    elif desc.shapeType == 'Polygon':
        buffDist = '-750 feet'
    arcpy.Buffer_analysis(in_features = featClass,out_feature_class = featClass + "_Buff",buffer_distance_or_field = buffDist)

    print featClass

print "Script Completed"



