import sys
import os
import subprocess
# working with arguements

print("Arguements List :" ,str(sys.argv))
# getting file name and path of the file

#getopt.getopt(args, options, [long_options])
#print(__file__)

input_file_path = "./input/output-1.jpg"
output_file_path = "./output/output"

command = "tesseract "+ input_file_path +" "+ output_file_path +" -l eng --oem 1 --psm 3"

print(command)
subprocess.run([command], shell= True)