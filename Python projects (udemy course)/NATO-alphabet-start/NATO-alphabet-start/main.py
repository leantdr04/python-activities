# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# students = {}
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     students += row.student
# print(students)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas

phonetics_df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in phonetics_df.iterrows()}

# print(phonetic_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("What is your name: ").upper()
phonetic_code = [phonetic_dict[letter] for letter in word]
print(phonetic_code)