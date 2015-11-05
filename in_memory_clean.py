import arcpy
from arcpy import env
sourceFC = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\multi_point"
select_poly = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\sample_in"
#from code
arcpy.MakeFeatureLayer_management(sourceFC, "sourceFC_fl")
arcpy.MakeFeatureLayer_management(select_poly, "select_parcel_fl")
arcpy.SelectLayerByLocation_management("sourceFC_fl", "INTERSECT", "select_parcel_fl")

hard_out_fc = "C:\Users\hoodj\Documents\ArcGIS\Default.gdb\multi_point_empty"
in_memory_fc = "in_memory" + "\\" + "in_memory_fc"
test_out = "C:\\Users\\hoodj\\Documents\\ArcGIS\\Default.gdb\\test_out_fc9"

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

for f in fields:
    print f.name

fieldnames = [field.name for field in fields if (field.name != dsc.OIDFieldName and field.name != "GlobalID") ]
#fieldnames = ["OBJECTID", "Shape", "last_edited_date", "GlobalID"]

with arcpy.da.SearchCursor("sourceFC_fl", fieldnames) as sCur:
    with arcpy.da.InsertCursor(in_memory_fc, fieldnames) as iCur:
        for row in sCur:
            iCur.insertRow(row)


feature_set = arcpy.FeatureSet("in_memory//in_memory_fc")

#for test
arcpy.CopyFeatures_management(feature_set, test_out)

arcpy.Delete_management("in_memory")

print "end"
