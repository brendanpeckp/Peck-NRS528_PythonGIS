
# Bonus Task 2 - Use os to make a directory in your root directory, add a subdirectory inside it, check if it is created,
# delete the subdirectory and the main directory. Check if the main directory exists, print "namrdir EXISTS" or "namrdir NOT EXISTS"

import os

# Create a directory
os.mkdir(r"C:\bananas")

os.mkdir(r"C:\bananas\oranges")

# Print directory contents
list1 = os.listdir(r"C:\bananas")

if "oranges" in list1:
    print("oranges EXISTS")
else:
    print("oranges NOT EXISTS")

# Remove directories, recursively, will delete entire file path - BEWARE
os.removedirs(r"C:\bananas\oranges")

list2 = os.listdir(r"C:")

if "bananas" in list2:
    print("bananas EXISTS")
else:
    print("bananas NOT EXISTS")

