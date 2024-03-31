######
## Instructions
######
# # 2. Push sys.argv to the limit
# # Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv, and does something to them.
## The rules:
# #
# # Minimum of three arguments to be used.
# # You must do something simple in 15 lines or less within the Python file.
# # Print or file generated output should be produced.
######
## Notes
######
## Q: What is sys.argv?
## A: sys means system. The system module allows me some additional functions to work in python.
## A: Perhaps the most important function is sys.argv, which will allow you to add commands to the interpreter
## from an external file. I use this when executing my Python code from a *.bat file, as you can write:
## "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" Step_3.py ARGUMENT1 ARUGMENT2
## Try executing the Step_2.bat file that I have provided
## print("My argument: " + str(sys.argv[1]))
## print("My argument: " + str(sys.argv[2]))
## print("My argument: " + str(sys.argv[3]))
## Q: What is a bat file?
## A: https://en.wikipedia.org/wiki/Batch_file "A batch file is a script file in DOS, OS/2 and Microsoft Windows.
## It consists of a series of commands to be executed by the command-line interpreter, stored in a plain text file.
## How does python script take inputs from bat files as commands?
## I drew a little diagram for myself. In summary; PyCharm is only used for editing and saving. The terminal runs the .py
## and retrieves from the .bat when the .py calls for it.
## What is an arguement?
## a single word in a .bat file.

import sys

print(sys.version)
print(sys.executable)

print(sys.argv[1])

print("cat: " + str(sys.argv[1]))
print("squid: " + str(sys.argv[2]))
print("dog: " + str(sys.argv[3]))

animal_list = ["cat, squid, dog"]