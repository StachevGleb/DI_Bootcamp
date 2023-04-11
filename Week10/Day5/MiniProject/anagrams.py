from anagram_checker import AnagramChecker
from string import ascii_letters

def menu():
    while True:
        print('Input word')
        # user_choice = input('Choose a menu option above: ').lower()
        while True:
            user_input = input('Please enter one word: ')
            not_chars = [char for char in user_input if char not in ascii_letters]

            if len(user_input.split(' ')) > 1:
                print('More than one word prohibited.')

            if not_chars:
                print('Invalid characters')

            else:
                user_input.strip()
                result = AnagramChecker()
                is_valid = result.is_valid_word(user_input)
                anagrams = result.get_anagrams(user_input)
                print(anagrams)

                if is_valid:
                    print(f'{user_input} is a valid word.')
                    print(f'Anagrams: {", ".join(anagrams)}')
                else:
                    print(f'{user_input} Invalid word.')



menu()