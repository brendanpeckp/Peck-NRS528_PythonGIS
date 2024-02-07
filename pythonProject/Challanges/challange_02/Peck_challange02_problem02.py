##### 2. List overlap
##
## Using these lists:
##
## ```python
## list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
## list_b = ['dog', 'hamster', 'snake']
## ```
##
## 1. Determine which items are present in both lists.
## 2. Determine which items do not overlap in the lists.

## Item 1
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# print(list(set(list_a).intersection(list_b)))
## Found answer @ https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists
## from answer:
## >>> list1 = [1,2,3,4,5,6]
## >>> list2 = [3, 5, 7, 9]
## >>> list(set(list1).intersection(list2))
## [3, 5]

## Item 2
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# print(list(set(list_a).difference(list_b)))