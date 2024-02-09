
#####
# Step 6 - Using Functions to block code
#####

# A simple function:
# def square(x): # def allows you to name a block of code. You can use the name later to invoke that block of code.
#     y = x ** 2
#     return y
# # Now that our variable "y" is wrapped into the function named "square", you can not refer to "y" unless you say "return" and then store it in another variable.
# print(square(3))
# print(square(8347329))

# Function with multiple arguments
def string_parser(string, n):
    while string:
        yield string[:n]
        string = string[n:]
print(list(string_parser("1234567890",2)))

