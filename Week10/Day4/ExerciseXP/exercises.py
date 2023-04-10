# Exerscise 1

import random

def get_words_from_file():
    with open('wordlist.txt', mode='r') as file:
        content = file.readlines()
        return content

def get_random_sentence(length):
    random_words = []
    while len(random_words) < length:
        random_words.append(random.choice(get_words_from_file()).strip())
    return ' '.join(random_words).lower()


def main():
    print('Description:\n')

    try:
        length = int(input('Please enter number of words? '))

        while True:
            if length >= 2 and length <= 20:
                sentence = get_random_sentence(length)
                print(sentence)
                break
            else:
                raise ValueError
    except ValueError:
        print(f'{ValueError}\nAcceptable values: integer between 2 and 20.')

main()


# Exerscise 2



# import json
# json1 = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

 


# json_dict = json.loads(json1)
# print(json_dict['company']['employee']['payable']['salary'])

# with open('file.json', mode='w') as f:
#     json.dump(json_dict, f, indent=2)