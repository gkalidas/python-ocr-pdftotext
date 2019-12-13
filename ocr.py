import sys
import os
import subprocess
from os import listdir
from os.path import isfile, join
# working with arguements

print("Arguements List :" ,str(sys.argv))
# getting file name and path of the file

#getopt.getopt(args, options, [long_options])
#print(__file__)

input_file_path = "./input"

#extracting file-name from path
# head, tail = os.path.split(input_file_path)
# print("File name : ",tail)

#getting only all the files into a list
only_files = [f for f in listdir(input_file_path) if isfile(join(input_file_path, f))]

print("There are {} files in the list ".format(len(only_files)))

for i, x in enumerate(only_files):
    print("File {}: {} ".format(i,x))

    #converting each file into jpg

# output_file_path = "./output/output"
# command = "tesseract "+ input_file_path +" "+ output_file_path +" -l eng --oem 1 --psm 3"
# subprocess.run([command], shell= True)