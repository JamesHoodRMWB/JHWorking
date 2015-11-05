import arcpy
from arcpy import env
multi_point = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\multi_point"
select_poly = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\sample_in"
#from code
arcpy.MakeFeatureLayer_management(multi_point, "multi_point_fl")
arcpy.MakeFeatureLayer_management(select_poly, "select_parcel_fl")
arcpy.SelectLayerByLocation_management("multi_point_fl", "INTERSECT", "select_parcel_fl")

fields_list = []

## field list
#fields = arcpy.ListFields(multi_point)
#for f in fields:
    
    

address_list = []
#search iterates through selected features in feature layer EZ.


for row in arcpy.SearchCursor("multi_point_fl"):
    list_in = [row.OBJECTID, row.Shape, row.ADDRESS, row.COMMUNITY, row.STREET_NAME, row.STREET_NUMBER, row.STREET_NUMBER_SUFFIX, row.ST_DIRECTION, row.ST_NAME, row.ST_TYPE, row.UNIT, row.ROTATION_ANGLE, row.created_user, row.created_date, row.last_edited_user, row.last_edited_date, row.BASEMENT, row.BASEMENT_BEDROOMS, row.GlobalID]
    address_list.append(list_in)

#for addli in address_list:
#    print str(addli)



in_memory_fc = "in_memory" + "\\" + "myMemoryFeature"
test_out = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\test_out_fc3"

# Set workspace
env.workspace = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb"

# Set local variables
out_path = "in_memory"
out_name = "in_memory_fc"
geometry_type = "POINT"
template = multi_point
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_reference = arcpy.Describe(multi_point).spatialReference

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)

#insert cursor to add data to in memory fc
insert_cursor = arcpy.da.InsertCursor("in_memory//in_memory_fc", "*")

count = 0
for a in address_list:
    insert_cursor.insertRow(a)
    print a

#for test
feature_set = arcpy.FeatureSet("in_memory//in_memory_fc")
arcpy.CopyFeatures_management(feature_set, test_out)

arcpy.Delete_management("in_memory")

print "end"
