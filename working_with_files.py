#! /usr/bin/python
# File I/O -- 
# ref: https://www.tutorialspoint.com/python/python_files_io.htm
""" Demonstrates how to open, close, read and write files"""
from datetime import date, datetime
import os

# Define needed Variables:
stop_flag = False # Used to indicate if user want to execute code

# get the current time and date
now_time = datetime.now()

# define the name of the logfile. Note the \\
logfileName = ".\\logfiles\\logfile.txt"
# Check to see if logfile exists
if not(os.path.isfile(logfileName)):
    # Tell the user that the file does not exist
    print (f'{logfileName} does not exist... Should I create it?')
    file_answer = str.lower(input("Enter Y (default) or N:"))
    if file_answer =="" or file_answer =="y":
        stop_flag = False
    elif file_answer == "n": # User wants to stop the file
        stop_flag=True
    else:
        stop_flag = True
        print("You need to enter either Y or N")
# If file does not exist, file will be created 
# Open the file for writing
if not(stop_flag): # We do not want to stop the program
    obj_workingfile = open(logfileName, "w")
    print (f"*** File " + obj_workingfile.name + " has been opened in mode: " + obj_workingfile.mode)

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
    # Sample read the file line by line
    obj_workingfile = open(logfileName, "r")
    # Read to EOF
    #If file.read() returns an empty str, it is the EOF.
    while obj_workingfile.read() != "": 
        line_no = 1
        line_read = obj_workingfile.readline()
        print(f"*** Line {line_no}: {line_read}")
    obj_workingfile.close()
print ("*** Program completed......")
