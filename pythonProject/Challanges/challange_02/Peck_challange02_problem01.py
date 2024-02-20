## Problem 1
## Item 1
## 1. Make a new list that has all the elements less than 5 from this list in it and print out this new list.
## The List:
## ```python
## [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
## ```

List1 = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
List2 =[]
for elem in List1:
    # print(elem)
    if elem < 5:
        # print(elem)
        List2.append(elem)
print(List2)

## Item 2
## 2. Write this in one line of Python (you do not need to append to a list just print the output).
List1 = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
print([wetgrrgshh for wetgrrgshh in List1 if wetgrrgshh < 5]) # This is just an inside to outside, left to right notation
# This way, I can put the entire code in one line.
# The "wetgrrgshh" is just to remind me that I can name it anything. (I would not usually use a bizarre name like that)

