
# Task - Use os.system to make a directory in your current directory, check if it is created
# delete it and check again.

import os

makedir = os.system("mkdir test_dir")
check_dir = os.system("dir")
os.system("rmdir test_dir")
os.system("dir")