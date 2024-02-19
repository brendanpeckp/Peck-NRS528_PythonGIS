## Problem 1
## Item 1
## 1. Make a new list that has all the elements less than 5 from this list in it and print out this new list.
## The List:
## ```python
## [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
## ```
List1 = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
for i in List1:
    if i == 6:
        List1.remove(i)
for i in List1:
    if i == 8:
        List1.remove(i)
for i in List1:
    if i == 12:
        List1.remove(i)
for i in List1:
    if i == 20:
        List1.remove(i)
for i in List1:
    if i == 32:
        List1.remove(i)
for i in List1:
    if i == 46:
        List1.remove(i)
for i in List1:
    if i == 85:
        List1.remove(i)
        print(List1)
## Item 2
## 2. Write this in one line of Python (you do not need to append to a list just print the output).
## Attempt 1
# List1 = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# for elem in List1:
#     if elem < 5:
#         print(elem)
## Attempt 2
List1 = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
List2 =[]
for elem in List1:
    print(elem)
    if elem < 5:
        print(elem)
        List2.append(elem)
        # for elem in List1:
        #     if elem > 5:
        #         List1.remove(elem)
        #         for elem in List1:
        #             if elem > 5:
        #                 List1.remove(elem)
print(List2)
## Success for both items? Yes for 1. No for 2.

List1 = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
print([element for element in List1 if element < 5])