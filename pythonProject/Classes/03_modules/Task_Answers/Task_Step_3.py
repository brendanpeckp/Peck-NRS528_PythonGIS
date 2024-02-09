
# Task - Using the provided text file Task_Step_3.txt, within the Tasks directory, iterate through the
# existing file, and find which line numbers the following words are on: Limpet, Mongoose, Spider monkey,
# Zebra. Hint, you will likely fail to match the whole word, as a new line is appended in the file, so
# as you iterate through each line you should match line.rstrip(), as this removes the \n


animal_file = open("Task_Step_3.txt", "r")

match_list = ["Limpet", "Mongoose", "Spider monkey", "Zebra"]
line_counter = 1

for line in animal_file.readlines():
    if line.rstrip() in match_list:
        print(line.rstrip() + " is on line: " + str(line_counter))
    line_counter = line_counter + 1

animal_file.close()