# with open("./weather_data.csv", "r") as data_file:
#     weather_list = data_file.readlines()
#     print(weather_list)
#
# import csv
# from itertools import islice
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in islice(data, 1, None):
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
