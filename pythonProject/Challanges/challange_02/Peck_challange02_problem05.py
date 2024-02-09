### 5. User input 2
##
## Using the following dictionary (or a similar one you found on the internet), ask the user for a word, and compute the *Scrabble* word score for that word (Scrabble is a word game, where players make words from letters, each letter is worth a point value), steal this code from the internet, format it and make it work:
##
## ```python
## letter_scores = {
##     "aeioulnrst": 1,
##     "dg": 2,
##     "bcmp": 3,
##     "fhvwy": 4,
##     "k": 5,
##     "jx": 8,
##     "qz": 10
## }
## ```
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }
# print(dict(letter_scores))
# def letterScore(let):
#     """Argument let: one character string
#     Return Value: the scrabble value of the letter"""
#     if let in 'qz':
#         return 10
#     elif let in 'aelnorstu':
#         return 1
#     elif let in 'd':
#         return 2
#     elif let in 'bcmp':
#         return 3
#     elif let in 'vwy':
#         return 4
#     elif let in 'k':
#         return 5
#     elif let in 'x':
#         return 8
#     else:
#         return 0
# word = input("What is your word? ") # gets a word from the user to score later.
# print(str(word)) # Check
# letters_of_word = word.split() # I want this to split the input word into letters.
# print(letters_of_word)

SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10} # this is a dictionary. It holds a score value for each letter that may be in a word.
total = 0 # Later when you add scores, you need something to add to. They will be added to the total.
# word = "panda" # This variable is equal to my example word. Change this to user input later.
word = input("What is your word? ") # This variable will be equal to whatever word the user inputs.
for letter in word: # IDK how it knows what a letter is but it does. Anyway, this tells it to look for letters in the word.
    total += SCORES[letter] # preset total + a letter from the SCORES dictionary. Then, again from each latter in the example word.
print(total)
