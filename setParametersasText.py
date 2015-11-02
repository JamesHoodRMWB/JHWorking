import arcpy

inputText = arcpy.GetParameterAsText(0)

arcpy.AddMessage("I have  arcpy.AddMessage("")")

inputNumber1 = arcpy.GetParameterAsText(1)
inputNumber2 = arcpy.GetParameterAsText(2)


output = int(inputNumber1) + int(inputNumber2)

arcpy.AddMessage(str(output))

arcpy.AddMessage(inputText)

