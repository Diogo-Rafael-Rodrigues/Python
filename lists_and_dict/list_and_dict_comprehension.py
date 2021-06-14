# List comprehension

names = ["Alex", "Beth", "Marcia", "DiegoGab"]
long_name = [letter.upper() for letter in names if len(letter) > 4 ]
print(long_name)

# using range
new_list = [n  for n in range(0,6,2)]
print(new_list)
[0, 2, 4]

new_list = [n * 2  for n in range(0,6)]
print(new_list)
[0, 2, 4, 6, 8, 10]

# using strings
list = "Diogo"
new_list = [n + n for n in list]
print(new_list)
['DD', 'ii', 'oo', 'gg', 'oo']

list = "Diogo"
new_list = [n + "a" for n in list]
print(new_list)
['Da', 'ia', 'oa', 'ga', 'oa']

# using numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

# using files
with open("file1.txt") as file_1:
  file_1_data = file_1.readlines()
with open("file2.txt") as file_2:
  file_2_data = file_2.readlines()

result = [int(n) for n in file_1_data if n in file_2_data]
print(result)

result = [int(n) for n in file_1_data if n not in file_2_data]
print(result)


# Dictionary comprehension
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}

# discovering the lenght of the words
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {words:len(words) for words in sentence.split()}

print(result)

#Turning °C in °F
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {days:temp * 9/5 + 32 for (days, temp) in weather_c.items()}

print(weather_f)

#using Pandas
import pandas

student_dict = {
  "student": ["Angela", "James", "Lily"]
  "score": [56, 76, 90]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#looping through rowns of a data frame

for (index, row) in student_data_frame.iterrows():
  #print(index)  or print(row) if nessecery
  print(row.student) # print(row.score)

  # I can even
    if row.student == "Angela":
      print(row.score)