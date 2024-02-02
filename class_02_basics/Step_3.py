#
# #####
# # Step 3 - Variables and data types
# #####
#
# # # This is bad variable naming:
# # x = r'C:\Shapefile.shp'
# # print(gobshite)
#
# # # # This is not valid, as variables cannot start with a number nor can they contain spaces:
# # x = r'C:\Shapefile.shp'
# # print(x)
# # x1 = r'C:\Shapefile.shp'
# # print(x1)
# # #
# # # Best practice variable naming:
# # input_file_path = r'C:\Shapefile.shp'
# # inputFilePath = r'C:\Shapefile.shp'
# # inputFilePathString = r'C:\Shapefile.shp'
# #
# # #####
# # # Data types
# # #####
# #
# # # String
# # example_string = 'this is a string, it can store anything... Well almost'
# # example_string = 'you cannot use the same 'quote' mark within a string'
# # example_string = 'but you can use this: "quote"'
# # example_string = "or this 'quote'"
#
# # example_string = 'escaping slashes is also an issue, \''
# # example_string = r'using the r letter (raw string) prior to the string ignores it-> \'
# #
# # # You can declare a string using str()
# # example_string = str('this is a string, but I would be anyway without str()')
# #
# # # You can join strings -
# example_string = 'Python'
# example_join_string = example_string + ' ' + '.. Magic!'
# print(example_join_string)
# # But you can only join strings, this will fail:
# example_join_string = example_string + ' ' + str(2) + '.. Magic!'
# print(example_join_string)
# example_join_string = example_string + ' ' + str(2) + '.. Magic!'
# #
# # # Integer
# example_integer = 2
# # # You can also declare an integer type-
# example_integer = int(2)
# not_an_integer = int(str('I am not an int'))
# # Be wary when computing using int:
# # print(int(5 / 2)) # = 2.5? Not according to Python, as it uses the floor value, and doesn't change datatype to float
# #
# # # Floats
# # print(5.0 / 2) #As the first value is float, it will work, and give the correct answer
# # print(5 / 2.0) #As the second value is float, it will work, and give the correct answer
# # print(5/2)
# # # # You can use round to round numbers, the first argument is the number, and the second the decimal places:
# # print(round(2.858, 1))
# # # # You can convert int to float to allow it to be used in calculation
# # print(float(int(2)))
# #
# # Lists
#
# # You can initiate a blank list:
# # my_blank_list = []
# #
# # # Or populate your list with variables
# my_first_list = ['item 1', 'item 2', 'item 3', 4, 5., ['a', 'b']]
# # # You can easily iterate through your list, see what happens to your list within a list though
# # for i in my_first_list: print(i)
# # # You can query an item within a list:
# # print(my_first_list[0]) #Note that zero notation, 0 = first item in list
# #
# # # You can add items to an exisiting list
# my_first_list.append('You added me later!')
# print(my_first_list)
# #
# # You can also merge two lists:
# list_1 = ['a', 'b', 'c']
# list_2 = ['alpha', 'beta', 'gamma']
# list_1.extend(list_2)
# #
# # # You can also order lists
# number_list = [1, 3, 4, 2]
# number_list.sort() #Ascending
# # print(number_list)
# # number_list.sort(reverse=True) #Descending
# # print(number_list)
# # #
# # # # You may remove items from a list, by index, slice or by variable content
# # del number_list[0]
# # print(number_list)
# #
# # del number_list[1:2]
# # print(number_list)
#
# number_list.remove(1)
# print(number_list)
#
# # # Tuples - Like lists but use () instead of [] and can't be changed after creation
# my_first_tuple = (1, 2, 3)
# print(my_first_tuple)
# #
# # # Tuples are immutable, cannot be changed after creation, try and see:
# my_first_tuple.append(4)
# #
# #
# # Dictionaries - Used to store values in a key:value pair
my_first_dictionary = {'key1':'Hi', 'Key2':'Bye'}
print(my_first_dictionary['Key2'])
#
# # You can't access a value or a key using an index:
# print(my_first_dictionary[0]) #not gonna work
#
# # More complex dictionary:
my_second_dictionary = { 1 : [{'Distance': '23', 'Density':'9'}], 2 : [{'Distance': '50', 'Density':'10'}], 3 : [{'Distance': '12', 'Density':'3'}] }
print(my_second_dictionary[1])
print(my_second_dictionary[1][0]['Distance'])
print(my_second_dictionary[1][0]['Density'])


###
# Brendan's Notes
###
# "print(x)" is a terrible name
# Research coding styles
# What is a string? :: It is a list of characters. It can be anything. It can be a number, name, file name, a point, whatever. It is named as "Str"
# We've done strings, integers, floats, del, and rounds.
# Squiggly brackets mean dictionaries.