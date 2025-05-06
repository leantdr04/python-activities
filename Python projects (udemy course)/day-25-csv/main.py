import csv
import pandas

# with open("weather_data.csv") as data_file:
#     temperatures = []
#     data = csv.reader(data_file)
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()

# average = sum(temp_list)/len(temp_list)
# print(average)
# # or data["temp"].mean()
# print(data["temp"].max())

# print(data.day)
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# mon_temp_F = monday_temp * 9/5 + 32
# print(mon_temp_F)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

count_df = pandas.DataFrame(data_dict)
count_df.to_csv("squirrel_count.csv")