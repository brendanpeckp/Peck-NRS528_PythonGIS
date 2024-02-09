
#####
# Step 4 - Iteration
#####

# For Loops

# # For loop on string
# my_string = 'abcde' # this has ''
# for i in my_string: # for loop
#     print(i) # print!
# #
# # # For loop on list
# my_list = ['a', 'b', 'c', 'd', 'e'] # this has []
# for i in my_list: # you can put a loop inside this loop
#     print(i)

# # For loop on tuple
# my_tuple = ('a', 'b', 'c', 'd', 'e') # tuples cannot be modified.
# for i in my_tuple:
#     print(i)

# For loop on dictionary
# my_dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# for i, j in my_dictionary.items():
#     print(i, j)


# If/else/elif

# You can use if/else/elif to make decisions based on your data:
# my_var = 5
# if my_var > 6: # if is a test. The computer takes my_var and tests if it is > 6. Then it sends to the options.
#     print('Greater than 6')
# elif my_var == 5: # else if, this is a secondary 'if' if the first if was not met.
#     print('Equal to 5')
# else: # if not meeting the if not the elif, then will hit else.
#     print('Less than 5') # You can do this with just an if.
##
# # Using if to catch cases as we loop:
# my_if_list = [1, 2, 3, 4, 5, 6]
# for i in my_if_list:
#     if i % 2 == 0: # this is a test. Can i be divided by 2? The computer will return a 1 for no and 0 for yes.
#         print(str(i) + ' is even because we can divide it by two')
#     else:
#         print(str(i) + ' is odd because it will not divide by two')


# While

# We can use while to perform some task
i = 0
while i < 10: # while is like if, but it stops looping when the test is no. In this case
    i = i+1
    print(i)

# # Be careful though not to enter an infinite loop as you forgot your increment
# i = 0
# while i < 10:
#     print(i)


