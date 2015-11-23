import arcpy

# A list of features and coordinate pairs
#
coordList = [[[1,2], [2,4], [3,7]],
            [[6,8], [5,7], [7,2], [9,5]]]

# Create empty Point and Array objects
#
point = arcpy.Point()
array = arcpy.Array()

# A list that will hold each of the Polygon objects 
# 
featureList = []

for feature in coordList:
    # For each coordinate pair, set the x,y properties and add to the 
    #  Array object.
    #
    for coordPair in feature:
        point.X = coordPair[0]
        point.Y = coordPair[1]
        array.add(point)

    # Add the first point of the array in to close off the polygon
    #
    array.add(array.getObject(0))

    # Create a Polygon object based on the array of points
    #
    polygon = arcpy.Polygon(array)

    # Clear the array for future use
    #
    array.removeAll()

    # Append to the list of Polygon objects
    #
    featureList.append(polygon)

# Create a copy of the Polygon objects, by using featureList as input to 
#  the CopyFeatures tool.
#
arcpy.CopyFeatures_management(featureList, "c:/geometry/polygons.shp")
