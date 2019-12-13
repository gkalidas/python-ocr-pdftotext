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

all_input_file_path = "./input"

#extracting file-name from path
# head, tail = os.path.split(input_file_path)
# print("File name : ",tail)

#getting only all the files into a list
only_files = [f for f in listdir(all_input_file_path) if isfile(join(all_input_file_path, f))]
#print("There are {} files in the list ".format(len(only_files)))

for index, input_file in enumerate(only_files):
    #print("File {}: {} ".format(index,input_file))

    #converting each file into jpg
    #convert -density [150-300] GaneshLondhe.pdf GaneshLondhe.jpg

    input_file_path = all_input_file_path + "/" +  input_file
    #print(" Input file path : " ,input_file_path)

    head, tail = os.path.splitext(input_file)
    output_file_name = "./temp/" + head + '.jpg'

    #ERROR 1

    command = "convert -density 150 "+ input_file_path +" "+ output_file_name +""
    subprocess.run([command], shell = True)

# output_file_path = "./output/output"

# how to run a command line statement inside python file
# command = "tesseract "+ input_file_path +" "+ output_file_path +" -l eng --oem 1 --psm 3"
# subprocess.run([command], shell= True)