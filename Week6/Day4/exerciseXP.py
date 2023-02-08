# Exercise 1
my_fav_numbers = {1, 2, 3}
my_fav_numbers.add(4)
my_fav_numbers.add(5)
my_fav_numbers.remove(5)
print(my_fav_numbers)
friend_fav_numbers = {6, 7, 8}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2
# tuple is immutable
tup = (1, 2, 3, 4, 5)
print(tup)

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list.
print(basket)
basket.pop(0)
print(basket)
# Remove “Blueberries” from the list.
basket.pop(2)
print(basket)
# Add “Kiwi” to the end of the list.
basket.append('Kiwi')
print(basket)
# Add “Apples” to the beginning of the list.
basket.insert(0, 'Apples')
print(basket)
# Count how many apples are in the basket.
y = 0
for x in basket:
    if x == 'Apples':
        y += 1
print(y)
# Empty the basket.
basket.clear()
print(basket)

# Exercise 4
# Recap – What is a float? What is the difference between an integer and a float?
# int - digits without point instead of float which is with point
# Can you think of another way to generate a sequence of floats?
# my_list = []
# i = 10
# while i > 0:
#     import random
#     i = i - 1
#     x = (round(random.random(), 2))
#     my_list.append(x)
# print(my_list)

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# my_seq = []
# a = 1.5
# my_seq.append(a)
# print(my_seq)
# i = 0
# y = 1.5
# while i < 7:
#     i = i + 1
#     y = y + 0.5
#     my_seq.append(y)
# print(my_seq)

# Exercise 5
# Use a for loop to print all numbers from 1 to 20, inclusive.
i = 0
my_list2 = []
while i < 21:
    my_list2.append(i)
    i = i + 1
# print(my_list2)
# Using a for loop, that loops from 1 to 20(inclusive),
# print out every element which has an even index.
for x in my_list2:
    if x % 2 == 0:
        print(x)

# Exercise 6
# user_name = input('Your name, please: ')
# check = True
# while check:
#     if user_name == "Gleb":
#         print("Correct name !")
#         check = False
#     else:
#         check = True
#         user_name = input('Your CORRECT name, please: ')

# Exercise 7
# Ask the user to input their favorite fruit(s) (one or several fruits).
# user_fruits = input("Please, tell us your favorite kinds of fruits (separate the fruits with a single space): ")
# # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# fruits = user_fruits.split(" ")
# print(fruits)
# # Now that we have a list of fruits, ask the user to input a name of any fruit.
# user_fruit = input("Please, tell us your one favorite fruit: ")
# # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits!
# # Enjoy!”.If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# for x in fruits:
#     if x == user_fruit:
#         print("You chose one of your favorite fruits! Enjoy!")
#     else:
#         print("You chose a new fruit. I hope you enjoy")

# Exercise 8
# # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’
# # stop asking for toppings.
# user_input = input("Please, insert pizza toppings that you want: ")
# user_list = []
# user_list.append(user_input)
# while user_input != "quit":
#     user_input = input("One more ? insert pizza toppings that you want: ")
#     user_list.append(user_input)
#     print(user_input)
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# c = ', '.join(user_list)
# print(f"Message saying you’ll add {c} topping to their pizza")
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is
# # (10 + 2.5 for each topping).
# print(f"Your toppings: {c}. Total price: {(len(c) * 2.5) + 10}")

# Exercise 9
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
#
# Store the total cost of all the family’s tickets and print it out.
#
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


