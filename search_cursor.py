import arcpy

fc = r"C:\Users\hoodj\Documents\ArcGIS\Default.gdb\sample_titles"
outfc = r"C:\Users\hoodj\Documents\ArcGIS\Default.gdb\sample_out_titles2"


#fields = ["Title_no", "Owner_coun"]

#for search
dsc = arcpy.Describe(fc)
fields = dsc.fields
fieldnames = [field.name for field in fields if (field.name != dsc.OIDFieldName and field.name != "GlobalID") ]

#print fieldnames

#for insert
dsc2 = arcpy.Describe(outfc)
fields2 = dsc.fields
fieldnames2 = [field.name for field in fields2 if (field.name != dsc.OIDFieldName and field.name != "GlobalID") ]

#print fieldnames2

#for f in fieldnames:
#    print f

# For each row print the WELL_ID and WELL_TYPE fields, and the
#  the feature's x,y coordinates
##
##with arcpy.da.SearchCursor(fc, fieldnames) as sCur:
##    with arcpy.da.InsertCursor(outfc, fieldnames) as iCur:
##        for row in sCur:
##            pid = row[1]
##            owner_count = row[4]
##            name = row[5]
##            print pid, owner_count, name
##            #print "----------PID --------Owner_1-----------Owner_1_A----------Owner_1_Po----------Owner_1_Pr"
##            row.setValue("PID", pid)
##            row.setValue("Owner_1", name)
##            iCur.updateRow(row)
            
##valueslist = []
##
##with arcpy.da.SearchCursor(fc, fieldnames) as sCur:
##    for row in sCur:
##        pid = row[1]
##        owner_count = row[4]
##        name = row[5]
##        print pid, owner_count, name
##        valueslist.append(pid, owner_count, name)
##        
##
##with arcpy.da.InsertCursor(outfc, fieldnames) as iCur:
##    for irow in iCur:
##        
##        iCur.updateRow(irow)


##with arcpy.da.SearchCursor(fc,fieldnames) as sCur:
##    with arcpy.da.InsertCursor(outfc,fieldnames) as iCur:
##        
##        for row in sCur:
##            ownercount = row[4]
##            iCur.insertRow(row)
##            if ownercount == 2:
##                #insert values
##                if ownercount == 3:
##                    #insert values
##                    if ownercount == 4:
##                        #insert values
##                        if ownercount == 5:
##                            #insert values


                
