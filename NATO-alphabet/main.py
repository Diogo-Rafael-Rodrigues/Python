import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

list_of_names = pd.read_csv('nato_phonetic_alphabet.csv', header=None, index_col=0, squeeze=True).to_dict()
#print(list_of_names)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Digite seu o nome a ser traduzido").upper()
output_list = [list_of_names[letter] for letter in word]
print(output_list)
