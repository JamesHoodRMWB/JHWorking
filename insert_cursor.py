import arcpy

# A list of values that will be used to construct new rows
#
row_values = [('Point1', (471567, 6290497)),
              ('Point2', (471568, 6290498))]

# Open an InsertCursor
cursor = arcpy.da.InsertCursor("C:\Users\hoodj\Documents\ArcGIS\Default.gdb\insert_point",
                               ("NAME", "SHAPE@XY"))

# Insert new rows that include the county name and a x,y coordinate
#  pair that represents the county center
#
for row in row_values:
    cursor.insertRow(row)

# Delete cursor object
#
del cursor

print "end"


"""Using the above methods --  arcpy.da.InsertCursor -- I could in theory use the following work flow to make this work:
1: feature class points in_memory
2: ad X and Y fields
3: Calculate x and y gemoetries into fields
4: create list of X and Y fields and unique identifier
5: use insert cursor above to add these geometries to the in_memory FC
6: use update cursor to add field values for the remaining fields.

Currently using da.update cursor I cannot figure out had to create the geometry without having an x,y array.
Additionally, I cannot seem to figure out how to add more information other than the single string field before the  x,y array.

Here is a sample from stack exchange that might work.
http://gis.stackexchange.com/questions/90372/using-arcpy-da-insertcursor-to-insert-an-entire-row-that-is-fetched-from-a-searc.
I will try this in a seperate script.  see da.insertcursor.py

On a related note, I attempted to look at arcpy.insert.cursor (no da), this appears to be an older version and could have potential
but the only example I could find involves creating new rows in a table, it does not seem to create geometries. """
