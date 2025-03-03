# with open("weather_data.csv") as data_dile:
#     data = data_dile.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')

# print(data)
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()

#Average
# print(data["temp"].mean())
#
# # Max
# print(data["temp"].max())
#
# #get data in columns
# print(data["condition"])
#
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [55, 65, 74]
}

data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")
