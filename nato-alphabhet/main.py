import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

incorrect_input = True

while incorrect_input:
    try:
        user_word = input('Enter a word: ').upper()
        phonetic_code = [nato_alphabet_dict[letter] for letter in user_word]
        print(phonetic_code)
        incorrect_input = False
    except KeyError:
        print('Sorry, only letters please.')
        user_word = input('Enter a word: ').upper()

