# File I/O -- 
# ref: https://www.tutorialspoint.com/python/python_files_io.htm
""" Demonstrates how to open, close, read and write files"""
from datetime import date, datetime
import os
# get the current time and date
now_time = datetime.now()
# define the name of the logfile. Note the \\
logfileName = ".\\logfiles\\logfile.txt"
# Check to see if logfile exists
if not(os.path.isfile(logfileName)):
    # the file does not exist so create it
    print (f'{logfileName} does not exist... creating...')
# File will be created when opened for writing
obj_workingfile = open(logfileName, "w")
print (f"File " + obj_workingfile.name + " has been opened in mode: " + obj_workingfile.mode)

# Then open the existing file
#try:
#    obj_workingfile = open("logfile.txt", "w")
#except:
    # Open failed, so we assume that the file does not exist
    # and we will create it

# Write one line to the file
# Write does not automatically add newlines
obj_workingfile.write("Logfile Begins at:" + str(now_time) + "\n")
obj_workingfile.write(str(datetime.now()) + " :: This is the second line of the file")
# Close the open file -- it's important you do this!
obj_workingfile.close()

# Reading Files
obj_workingfile = open(logfileName, "r")
# () contains the number of bytes (characters) to be read
# if omitted, it reads as much as it can - most likely to the
# end of the file.
items_read = obj_workingfile.read()
print (f"***Read the following: {items_read}")
obj_workingfile.close()
obj_workingfile = open(logfileName, "r")
line_read = obj_workingfile.readline()
print(f"*** Read one line: {line_read}")
obj_workingfile.close()
print ("*** Program completed......")
