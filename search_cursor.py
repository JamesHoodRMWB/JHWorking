import arcpy

fc = r"C:\Users\hoodj\Documents\ArcGIS\Default.gdb\sample_titles"

#fields = ["Title_no", "Owner_coun"]

dsc = arcpy.Describe(fc)
fields = dsc.fields
fieldnames = [field.name for field in fields if (field.name != dsc.OIDFieldName and field.name != "GlobalID") ]

#for f in fieldnames:
#    print f

# For each row print the WELL_ID and WELL_TYPE fields, and the
#  the feature's x,y coordinates

with arcpy.da.SearchCursor(fc, fieldnames) as cursor:
    for row in cursor:
        #print "----------PID --------Owner_1-----------Owner_1_A----------Owner_1_Po----------Owner_1_Pr"
        print ""
        print ""
        print str(row[1]) +" "+str(row[5]) +" "+ str(row[6]) + " " + str(row[7]) + " " + str(row[8])
        if row[4] != 1:
            print "entered if statement"
            count = row[4]
            print count
            loopvalue = 0
            while loopvalue != 2:
                print "     Second        " + str(row[9]) +" "+ str(row[10]) + " " + str(row[11]) + " " + str(row[12])
                loopvalue = 2

