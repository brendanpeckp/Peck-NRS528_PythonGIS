# Task - Using sys.argv write a small code block to read in 3 arguments to your Python file
# store each one in a list and iterate through them, printing each with the text "Argument 1 = ", "Argument 2 = ".
# Hint, you will need to edit the *.bat file to include the arguments.

import sys

argument1 = sys.argv[1]
argument2 = sys.argv[2]
argument3 = sys.argv[3]

argument_list = [argument1, argument2, argument3]
counter = 1

for i in argument_list:
    print("Argument " + str(counter) + " = " + str(i))
    counter = counter + 1

# *.bat file content = "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" Step_2.py Dog Cat Rabbit