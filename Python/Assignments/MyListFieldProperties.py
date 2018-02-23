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

field_list = arcpy.ListFields("MajorAttractions")

txtFile = open(os.path.join(wksp,"MajorAttractions.txt"),"w")
txtFile.write("MajorAttractions field information" + "\n")
txtFile.write("--------------------------------------------------" + "\n")

for field in field_list:
    line = "Name: {}, Type: {}, Length: {}\n".format(field.name,field.type,field.length)
    print line
    txtFile.write(line)

txtFile.close()

print "Script Completed"

os.popen(os.path.join(wksp,"MajorAttractions.txt"))

