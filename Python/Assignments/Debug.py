import arcpy

arcpy.AddMessage("Message1")
arcpy.AddWarning("Warning")
arcpy.AddError("Error")
arcpy.AddMessage("Message2")

Messages = arcpy.GetMessages(0)
Warnings = arcpy.GetMessages(1)
Errors = arcpy.GetMessages(2)

print "Messages: " + Messages
print

print "Warnings: " + Warnings
print

print "Errors: " + Errors
print

print "Script completed."
