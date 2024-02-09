
# Bonus Task 2 - Code your Scrabble score work from Coding Challenge 2 to use 3 sys.argv inputs

import sys

score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,  "f": 4,
         "g": 2, "h": 4,"i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4,"z": 10}


def scrabble_score(x):
    total = 0
    for letter in x:
        total += score[letter]
    return total


argument1 = sys.argv[1]
argument2 = sys.argv[2]
argument3 = sys.argv[3]

argument_list = [argument1, argument2, argument3]
counter = 1

for i in argument_list:
    print("Word " + str(counter) + " = " + str(i) + ", score = " + str(scrabble_score(str(i.lower()))))
    counter = counter + 1