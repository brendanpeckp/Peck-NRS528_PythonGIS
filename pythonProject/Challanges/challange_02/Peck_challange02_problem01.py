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
print([element for element in List1 if element < 5])