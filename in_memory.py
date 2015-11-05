import arcpy
from arcpy import env
sourceFC = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\insert_point" #"C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\multi_point"
select_poly = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\sample_in"
#from code
arcpy.MakeFeatureLayer_management(sourceFC, "sourceFC_fl")
arcpy.MakeFeatureLayer_management(select_poly, "select_parcel_fl")
arcpy.SelectLayerByLocation_management("sourceFC_fl", "INTERSECT", "select_parcel_fl")

#fields_list = []
#string_fields_list = []
## field list
#fields = arcpy.ListFields(multi_point)
#for f in fields:
#    string_field = str(f)
#    string_fields_list.append(string_field)
#string_fields_list = ["OBJECTID", "Shape", "ADDRESS", "COMMUNITY", "STREET_NAME", "STREET_NUMBER", "STREET_NUMBER_SUFFIX", "ST_DIRECTION", "ST_NAME", "ST_TYPE", "UNIT", "ROTATION_ANGLE", "created_user", "created_date", "last_edited_user", "last_edited_date", "BASEMENT", "BASEMENT_BEDROOMS", "GlobalID"]


arcpy.Delete_management("in_memory")


#address_list = []
#search iterates through selected features in feature layer EZ.


#for row in arcpy.SearchCursor("sourceFC_fl"):
#    list_in = [row.OBJECTID, row.Shape, row.ADDRESS, row.COMMUNITY, row.STREET_NAME, row.STREET_NUMBER, row.STREET_NUMBER_SUFFIX, row.ST_DIRECTION, row.ST_NAME, row.ST_TYPE, row.UNIT, row.ROTATION_ANGLE, row.created_user, row.created_date, row.last_edited_user, row.last_edited_date, row.BASEMENT, row.BASEMENT_BEDROOMS, row.GlobalID]
#    address_list.append(list_in)
#for addli in address_list:
#    print str(addli)

hard_out_fc = "C:\Users\hoodj\Documents\ArcGIS\Default.gdb\multi_point_empty"

in_memory_fc = "in_memory" + "\\" + "in_memory_fc"
test_out = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\test_out_fc6"

# Set workspace
env.workspace = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb"

# Set local variables
out_path = "in_memory"
out_name = "in_memory_fc"
geometry_type = "POINT"
template = sourceFC
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe(sourceFC).spatialReference

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)


#testing advanced insert script
dsc = arcpy.Describe(sourceFC)
fields = dsc.fields

fieldnames = [field.name for field in fields if field.name != dsc.OIDFieldName]

with arcpy.da.SearchCursor(sourceFC, fieldnames) as sCur:
    with arcpy.da.InsertCursor(in_memory_fc, fieldnames) as iCur:
        for row in sCur:
            iCur.insertRow(row)



#insert cursor to add data to in memory fc
#insert_cursor = arcpy.InsertCursor("in_memory//in_memory_fc", string_fields_list)
#for a in address_list:
#    insert_cursor.insertRow(a)
#    print a

#rows = arcpy.InsertCursor("in_memory//in_memory_fc")
#for a in address_list:
#    row = rows.newRow()
#    row.setValue("OBJECTID", a[0])
#    row.setValue("Shape", a[1])


#for test
feature_set = arcpy.FeatureSet("in_memory//in_memory_fc")
arcpy.CopyFeatures_management(feature_set, test_out)

arcpy.Delete_management("in_memory")

print "end"
