# Exercise 1

# def display_message():
#     print("Python")
# display_message()

# Exercise 2

# def favorite_book(book):
#     print(f"One of my favorite books is {book}")
# book = "Harry Potter"
# favorite_book(book)

# Exercise 3

# def describe_city(city, country):
#     print(f"{city} is in {country.capitalize()}")
# describe_city("TLV", country="israel")

# Exercise 4

# users_number = int(input("Please, insert number between 1 to 100: "))
# while users_number > 100 or users_number < 0:
#     users_number = int(input("Please, insert correct number between 1 to 100: "))
#
# def numbers_comparing(users_number):
#     from random import randrange
#     x = randrange(100)
#     if users_number == x:
#         print("Success")
#     else:
#         print(f"x equal to {x}")
#         print(f"users number equal to {users_number}")

# Exercise 5

# message = "Hello World"
# size = "XL"
# def make_shirt(message, size):
#     print(f"The size of the shirt is {size} and the text is {message}")
#
# make_shirt('I love Python', size = 'L')
# make_shirt(message = 'I love Python', size = 'L')
# make_shirt(message = 'I love Bootcamp', size = 'XXl')
# make_shirt('I love JS', size = 'S')

# Exercise 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for item in magician_names:
        print(item)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + ' the Great'
        print(i)
make_great(magician_names)
print(magician_names)
show_magicians(magician_names)

