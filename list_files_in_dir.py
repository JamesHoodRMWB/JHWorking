# list of files in a directory
import os

dir = r"C:\Users\hoodj\Desktop\Python_working\sub_sample"

fileList = os.listdir(dir)

for f in fileList:
    p = os.path.join(dir, f)
    print p

