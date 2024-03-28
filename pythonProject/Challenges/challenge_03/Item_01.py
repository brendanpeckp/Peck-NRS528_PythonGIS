## Replicate this tree of directories and subdirectories:
## ├── draft_code
## |   ├── pending
## |   └── complete
## ├── includes
## ├── layouts
## |   ├── default
## |   └── post
## |       └── posted
## └── site
## Using os.system or os.mkdirs replicate this simple directory tree.
## Delete the directory tree without deleting your entire hard drive.

######
## My Tools for Reference:
######

### Creating deleting, and reading folders in a local directory
# import os # The os package gives you functions that allow you to interface with the operating system:
# os.system("mkdir hello") # Creates a folder in my local (shared with Item_01.py's folder)
# os.system("dir") # Outputs a table that describes my local directory.
# os.system("rmdir hello") # Deletes file named "hello" in local directory.
# os.system("dir") # Reads local directory again. Notice that the hello folder is gone.

### Creating, deleting, and reading folders in your root directory.
## Create directories anywhere:
# import os # Gives required package
# file_path = r"C:\folder" # Creates a variable that represents the filepath you want to use.
# os.mkdir(file_path) # makes a directory in your named filepath.
# file_path2 = r"C:\folder\folder2" # defines a path inside the new folder.
# os.mkdir(file_path2) # creates a folder
## Check for directories anywhere:
# list1 = os.listdir(r"C:\folder")
# if "folder2" in list1:
#     print("folder2 EXISTS")
# else:
#     print("folder2 NOT EXISTS")
## Delete directories anywhere:
# os.removedirs(r"C:\folder\folder2") # removes the named directory and it's file path.
## Check again
# list2 = os.listdir(r"C:")
# if "folder" in list2:
#     print("folder EXISTS")
# else:
#     print("folder NOT EXISTS")

######
## My Item Submission
######
## I think that I will create all folders, check for all folders, then, delete all and check all.
## Heres a path naming key:
## I want to hold this entire tree in a seperate folder for neatness. I will hold them in C:\temporary_repository
## ├── draft_code       1
## |   ├── pending      1_1
## |   └── complete     1_2
## ├── includes         2
## ├── layouts          3
## |   ├── default      3_1
## |   └── post         3_2
## |       └── posted   3_2_1
## └── site             4

# Create
import os

# Path 0
file_path_0 = r"C:\temporary_repository"
os.mkdir(file_path_0)
# Path 1
file_path_1 = r"C:\temporary_repository\draft_code"
os.mkdir(file_path_1)
# Path 1_1
file_path_1_1 = r"C:\temporary_repository\draft_code\pending"
os.mkdir(file_path_1_1)
# Path 1_2
file_path_1_2 = r"C:\temporary_repository\draft_code\complete"
os.mkdir(file_path_1_2)
# Path 2
file_path_2 = r"C:\temporary_repository\includes"
os.mkdir(file_path_2)
# Path 3
file_path_3 = r"C:\temporary_repository\layouts"
os.mkdir(file_path_3)
# Path 3_1
file_path_3_1 = r"C:\temporary_repository\layouts\default"
os.mkdir(file_path_3_1)
# Path 3_2
file_path_3_2 = r"C:\temporary_repository\layouts\post"
os.mkdir(file_path_3_2)
# Path 3_2_1
file_path_3_2_1 = r"C:\temporary_repository\layouts\post\posted"
os.mkdir(file_path_3_2_1)
# Path 4
file_path_4 = r"C:\temporary_repository\site"
os.mkdir(file_path_4)

# Check
check_creation_of_folders = os.listdir(r"C:\temporary_repository\layouts\post")
if "posted" in check_creation_of_folders:
    print("posted EXISTS")
else:
    print("posted NOT EXISTS")

# Delete

# Path 4
os.removedirs(r"C:\temporary_repository\site")
# Path 3_2_1
os.removedirs(r"C:\temporary_repository\layouts\post\posted")
# # Path 3_2 # How come I didn't have to delete all individually? It seems that it will delete the mother folder in the case that it has no daughters.

# Path 3_1
os.removedirs(r"C:\temporary_repository\layouts\default")
# Path 3

# Path 2
os.removedirs(r"C:\temporary_repository\includes")
# Path 1_2
os.removedirs(r"C:\temporary_repository\draft_code\complete")
# Path 1_1
os.removedirs(r"C:\temporary_repository\draft_code\pending")
# Path 1

# Path 0


# Check again
check_removal_of_folders = os.listdir(r"C:")
if "temporary_repository" in check_creation_of_folders:
    print("temporary_repository EXISTS")
else:
    print("temporary_repository NOT EXISTS")