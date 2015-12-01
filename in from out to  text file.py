import os

# reads form a text file and outputs to a new text file.

inFile = "C:\Users\hoodj\Desktop\Python_working\inFile.txt"
outFile = "C:\Users\hoodj\Desktop\Python_working\outFile.txt"

text_variable = " and more text and "

outWrite = open(outFile, "w")


with open(inFile, "r") as readFile:

    for l in readFile:
        print l
        outWrite.write(" inserting text " + text_variable + l )



outWrite.close()
