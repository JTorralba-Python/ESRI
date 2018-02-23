import arcpy

point = arcpy.Point(2000, 1000)
print "Point X: {0}, Y: {1}".format(point.X, point.Y)

pnt = arcpy.Point()
ary = arcpy.Array()

coords = [[100, 200],[200, 400],[300, 600],[600, 800],[500, 700]]
for coord in coords:
    pnt.X = coord[0]
    pnt.Y = coord[1]
    ary.add(pnt)

polyLine = arcpy.Polyline(ary)
print "Number of points: {0}".format(polyLine.pointCount)

polygon = arcpy.Polygon(ary)
print "Number of points: {0}".format(polygon.pointCount)
