#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas


data = pandas.read_csv("weather_data.csv")
# print(type(data))  # pandas.core.frame.DataFrame
# print(type(data["temp"]))  # pandas.core.series.Series
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# # media = sum(temp_list) / len(temp_list)
# # print(media)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# data["condition"]
# print(data.condition)  # be aware about capital letters
#
# # Get Data in Row
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)


# CREATE A DATAFRAME FROM SCRATCH
data_dict = {
    "studants": ["Diogo", "Juliana", "Ricardo"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")