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

age = input("What is your age? ") # input means that the code will print and expect user input.
print("Your age is " + str(age) + ".")
yrs_till_retirement = 65 - int(age)
print("You have " + str(yrs_till_retirement) + " years till retirement.")