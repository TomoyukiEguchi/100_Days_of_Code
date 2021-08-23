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

# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday_row = data[data.day == "Monday"]
# celsius = int(monday_row.temp)
# print((celsius * 1.8) + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]

num_gray_squirrel = (len(gray_squirrel))
num_cinnamon_squirrel = (len(cinnamon_squirrel))
num_black_squirrel = (len(black_squirrel))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray_squirrel, num_cinnamon_squirrel, num_black_squirrel]
}

# print(data_dict)
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")