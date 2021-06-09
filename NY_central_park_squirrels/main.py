import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#  FIRST SOLUTION
# fur_color = data["Primary Fur Color"]
# gray_fur = 0
# cinnamon_fur = 0
# black_fur = 0
# fur_dict = fur_color.to_dict()
# for fur in fur_dict:
#     if fur_dict[fur] == "Gray":
#         gray_fur += 1
#     elif fur_dict[fur] == "Cinnamon":
#         cinnamon_fur += 1
#     elif fur_dict[fur] == "Black":
#         black_fur += 1
# print(gray_fur, cinnamon_fur, black_fur)

#  SECOND SOLUTION
gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, cinnamon_fur, black_fur]
}
squirrel_count = pandas.DataFrame(data_dict)
print(data)
squirrel_count.to_csv("squirrel_count.csv")


