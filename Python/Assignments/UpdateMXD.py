import arcpy.mapping as MAP

mxd = MAP.MapDocument(r"E:\Student\PYTH\Map_production\CorvallisMeters.mxd")

df = MAP.ListDataFrames(mxd)[0]

updateLayer = MAP.ListLayers(df, "ParkingMeters")[0]
sourceLayer = MAP.Layer(r"E:\Student\PYTH\Map_production\ParkingMeters.lyr")

MAP.UpdateLayer(df, updateLayer, sourceLayer, True)

addLayer = MAP.Layer(r"E:\Student\PYTH\Map_production\Schools.lyr")
MAP.AddLayer(df, addLayer)

refLayer = MAP.ListLayers(df, "Schools")[0]

MAP.MoveLayer(df, refLayer, updateLayer, "BEFORE")

mxd.title = "Corvallis Meters Map"
elemList = MAP.ListLayoutElements(mxd, "TEXT_ELEMENT")

for elem in elemList:
    if elem.name == "Corvallis Meters":
        elem.text = "Corvallis Parking Meters Inventory Report"

mxd.saveACopy(r"E:\Student\PYTH\Map_production\CorvallisMeters2.mxd")
#del mxd
