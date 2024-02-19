import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row['letter']: row['code'] for (index, row) in nato_alphabet.iterrows()}

user_word = input('Enter a word: ')
phonetic_code = [nato_alphabet_dict[letter] for letter in [letter.upper() for letter in user_word] if letter in nato_alphabet_dict]
print(phonetic_code)


