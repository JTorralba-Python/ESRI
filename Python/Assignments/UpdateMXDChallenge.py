import arcpy
import arcpy.mapping as MAP
import os, sys

mxd_dir = arcpy.GetParameterAsText(0)

if os.path.exists(mxd_dir) == False:
    sys.exit("1, Invalid path specified.  Re-run script with valid path.")

arcpy.env.workspace = mxd_dir

mxd_list = arcpy.ListFiles("*.mxd")

for name in mxd_list:
    mxdFile = os.path.join(mxd_dir, name)
    mxd = MAP.MapDocument(mxdFile)
    df = MAP.ListDataFrames(mxd)[0]

    updateLayer = MAP.ListLayers(df, "ParkingMeters")[0]
    sourceLayer = MAP.Layer(r"E:\Student\PYTH\Map_production\ParkingMeters.lyr")
    MAP.UpdateLayer(df, updateLayer, sourceLayer, True)

    addLayer = MAP.Layer(r"E:\Student\PYTH\Map_production\Schools.lyr")
    MAP.AddLayer(df, addLayer)

    refLayer = MAP.ListLayers(df, "Schools")[0]

    MAP.MoveLayer(df, refLayer, updateLayer, "BEFORE")

    elemList = MAP.ListLayoutElements(mxd, "TEXT_ELEMENT")
    mxd.title = "Corvallis Meters map"

    for elem in elemList:
        if elem.name == "Corvallis Meters":
            elem.text = "Central Park Meters"

    mxd_copy = name[:-4] + "_updated.mxd"
    mxd.saveACopy(os.path.join(mxd_dir, mxd_copy))
    #del mxd
