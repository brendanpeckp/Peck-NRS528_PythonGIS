### 4. User input
##
## Ask the user for an input of their current age, and tell them how many years until they reach retirement (65 years old).
##
## Hint:
##
## ```Python
## age = input("What is your age? ")
## print "Your age is " + str(age)
## ```

# age = range(1, 65)
# print(list(age))
# age = input("What is your age? ")
# # print ("Your age is " + str(age))

age = range(1, 65)
input(age)
while True:
    age = input("What is your age? ")
    if age == 65:
        break