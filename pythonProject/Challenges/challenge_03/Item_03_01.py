######
## Attempt Using Pandas
######

# I watched a tutorial on pandas because I know nothing on the topic. Once I have some base knowledge I can go ahead
# and complete the assignment.

import pandas as pd
# Imports Pandas which is a toolset (module? package?)
# Gives it the very standard alias of pd.

print(pd.read_csv("co2-ppm-daily (1).csv"))
# I can tell to read "co2-ppm-daily (1).csv" because that file is in this folder.
# If I wanted to have it read a file elsewhere I'd have to give it the absolute file path with an "r" at the start.
# My output thus far has a header.

dataframe = pd.read_csv("co2-ppm-daily (1).csv")
print(dataframe)
# A nice variable for my reading function.
# Dataframes are tables that pandas works with.

dataframe
# Call the table to save it?

dataframe_02 = pd.read_csv("co2-ppm-daily (1).csv")
print(dataframe_02)
# Make a 2nd dataframe so that I do not mess with the first one.

# dataframe_02.info()
# # Gives me some metadata on my dataframe.
#
# print(dataframe_02.head(10))
# # Prints the first 10 rows.
#
# print(dataframe_02.tail(10))
# # Prints the last 10 rows.
#
# print(dataframe_02.loc[3])
# # Tells me about the 3rd rank (4th row)