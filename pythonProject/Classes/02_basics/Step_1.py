
#####
# Step 1 - Commenting in Python
#####

# The hash symbol is used to create a single line comment.

# You can use
# multiple lines
# if you want

# You can also turn
# a block of code
# into a comment by
# using PyCharm:
# 1. Select your block of code.
# 2. Select "Code" from the menu bar.
# 3. Select "Comment with Line Comment".
# 4. You can also reverse this using the same steps 1-3.

# Block comments in the form of something like
# /*
#     This is a JavaScript style block comment
# */
#
# are not generally used in Python.


# Commenting style is very user dependent, I want you to attempt to comment
# the small code block below. What kind of information do you feel is pertinent?

######
###
#Peck's Notes on Andy's Lecture
###
#Use Ctrl + / to easily add or remove "#"
# Making variables:
# It can be anything but a number or begining with a number.
# The terms "inner" and "outer" refer to the sides of the loop,
# The outer part of the loop is the left side which is run (computer) and read (you) first.
# Outer, is done last.
# This for loop below will read/run left to right.
######

list1 = ['Hi', 'Hello', 'Allo']
list2 = ['Bye', 'Goodbye', 'Au Revoir']

for i in list1:
    for z in list2:
        print(i + ' but its not ' + z)

