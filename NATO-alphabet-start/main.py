import pandas

library_df = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dictionary = {row['letter']: row['code'] for (index, row) in library_df.iterrows()}


def generate_phonetic():
    user_input = input('Enter a word: ').upper()
    try:
        phonetic_word = [phonetic_dictionary[letter] for letter in user_input]
        valid_input = True
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()
