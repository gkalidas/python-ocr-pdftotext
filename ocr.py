import sys
import os
import subprocess
from os import listdir
from os.path import isfile, join

#getting number of pages in a pdf
from subprocess import check_output
# working with arguements

#print("Arguements List :" ,str(sys.argv))
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

def get_num_pages(pdf_path):

    # returns the number of pages from a given file

    output = check_output(["pdfinfo", pdf_path]).decode()
    pages_line = [line for line in output.splitlines() if "Pages:" in line][0]
    num_pages = int(pages_line.split(":")[1])
    return num_pages

total_pages = 0; total_files = len(only_files)

for input_file in only_files:
    input_file_path = all_input_file_path + "/" +  input_file
    a = get_num_pages(input_file_path)
    total_pages += a
    print("Input files {} contains {} pages.".format(input_file,a))

print("There are {} files and contains {} pages ".format(total_files,total_pages))

#for index, input_file in enumerate(only_files):
    #print("File {}: {} ".format(index,input_file))

    #input_file_path = all_input_file_path + "/" +  input_file
    #print(" Input file path : " ,input_file_path)

    # head, tail = os.path.splitext(input_file)
    # output_file_name = "./temp/" + head + '.jpg'

    # convert pdf to jpg for text recognization
    #You may encounter ERROR 1 here
    #command = "convert -density 150 "+ input_file_path +" "+ output_file_name +""
    #subprocess.run([command], shell = True)

# output_file_path = "./output/output"

# how to run a command line statement inside python file
# command = "tesseract "+ input_file_path +" "+ output_file_path +" -l eng --oem 1 --psm 3"
# subprocess.run([command], shell= True)