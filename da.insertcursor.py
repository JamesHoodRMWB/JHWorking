import arcpy, os


# Get field objects from source FC
#

sourceFC = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\multi_point"
targetFC = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\multi_point_empty"

dsc = arcpy.Describe(sourceFC)
fields = dsc.fields

# List all field names except the OID field
#
fieldnames = [field.name for field in fields if field.name != dsc.OIDFieldName]

# Create cursors and insert new rows
#
with arcpy.da.SearchCursor(sourceFC,fieldnames) as sCur:
    with arcpy.da.InsertCursor(targetFC,fieldnames) as iCur:
        for row in sCur:
            iCur.insertRow(row)

print "end"
