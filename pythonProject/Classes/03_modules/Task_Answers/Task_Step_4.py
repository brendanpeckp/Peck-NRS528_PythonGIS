
# Task - Using Step_4.csv, complete the following, 1) Make a list of the years and the countries in the dataset,
# how many years and countries are there? 2) Calculate the global population for every year in the dataset.
# 3) Split the global dataset into a file for each country, with the filename the name of the country, in a new
# directory using only Python


# 1) Make a list of the years and the countries in the dataset,
# how many years and countries are there?

import csv, os

country_list, year_list = [], []

with open("Task_Step_4.csv") as population_csv:
    headerline = population_csv.next()
    for row in csv.reader(population_csv):
        if row[0] not in country_list:
            country_list.append(row[0])
        if row[2] not in year_list:
            year_list.append(row[2])

print(len(country_list))
print(len(year_list))


# 2) Calculate the global population for every year in the dataset.

total_per_year = 0
total_pop_per_year_dict = {}

for y in year_list:
    with open("Task_Step_4.csv") as population_csv:
        for row in csv.reader(population_csv):
            if row[2] == y:
                total_per_year += int(float(row[3]))

    total_pop_per_year_dict[y] = total_per_year
    total_per_year = 0

print(total_pop_per_year_dict)


# 3) Split the global dataset into a file for each country, with the filename the name of the country, in a new
# directory using only Python

os.mkdir("Countries_Directory")

header = "Country Name,Country Code,Year,Population\n"

for c in country_list:
    c_count = 1
    with open("Task_Step_4.csv") as population_csv:
        for row in csv.reader(population_csv):
            if row[0] == c:
                if c_count == 1:
                    file = open(r"Countries_Directory/" + str(c) + ".csv", "w")
                    file.write(header)
                    c_count = 0
                #make well formmated line
                file.write(",".join(row))
                file.write("\n")
    file.close()


