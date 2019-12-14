import sys
import os
import subprocess
from os import listdir
from os.path import isfile, join
#getting number of pages in a pdf
from subprocess import check_output
#to calculate time
from timeit import default_timer as timer

################ ARGUEMENTS #######################
#print("Arguements List :" ,str(sys.argv))
# getting file name and path of the file
#getopt.getopt(args, options, [long_options])
#print(__file__)
#extracting file-name from path
# head, tail = os.path.split(input_file_path)
# print("File name : ",tail)

############### GLOBAL VARIABLES HERE #############
all_input_file_path = "./input"

#getting only all the files into a list
only_files = [f for f in listdir(all_input_file_path) if isfile(join(all_input_file_path, f))]

########################################################################
#################### COUNTING PAGES IN A PDF ###########################
########################################################################
# def get_num_pages(pdf_path):

#     # returns the number of pages from a given file

#     output = check_output(["pdfinfo", pdf_path]).decode()
#     pages_line = [line for line in output.splitlines() if "Pages:" in line][0]
#     num_pages = int(pages_line.split(":")[1])
#     return num_pages

########################################################################

total_pages = 0; total_files = len(only_files)

def to_text(
    path_to_jpg_files
    ):

    #print("path_to_jpg_files :", path_to_jpg_files)

    jpg_files = [f for f in listdir("./temp") if isfile(join("./temp", f))]

    for index, i_file in enumerate(jpg_files):
        input_file = "./temp/"+ i_file
        #print("working directory :",os.getcwd())
        #print("input file for tesseract is {}".format(input_file))
        #print("output file would be {}", output_file_path)
        o_file = os.path.splitext(i_file)[0]
        output_file_path = "./output/"+o_file
        #print(" output file name " ,o_file)
        command = "tesseract "+ input_file +" "+ output_file_path +" -l eng --oem 1 --psm 3"
        #print("command ", command)
        subprocess.run([command], shell= True)
        os.remove(input_file)
    #print("path_to_text :", path_to_text)

    
def to_jpg(
    input_file
    ):

    #convert each page from pdf file to jpg

    input_file_path = all_input_file_path + "/" +  input_file
    head, tail = os.path.splitext(input_file)
    output_file_name = "./temp/" + head + '.jpg'
    #ERROR 1
    
    command = "convert -density 150 "+ input_file_path +" "+ output_file_name+""
    subprocess.run([command], shell = True)

    #print("Done with {} forwarding to pdf".format(input_file_path))
    to_text(output_file_name)

for index, input_file in enumerate(only_files):
    #print("File {}: {} ".format(index,input_file))
    #input_file_path = all_input_file_path + "/" +  input_file
    #print(" Input file path : " ,input_file_path)
    to_jpg(input_file)


# output_file_path = "./output/output"

# how to run a command line statement inside python file
# command = "tesseract "+ input_file_path +" "+ output_file_path +" -l eng --oem 1 --psm 3"
# subprocess.run([command], shell= True)