# Challenge 1
# Ask the user for a number and a length.
# num = int(input("Please, insert your number ? : "))
# lnth = int(input("Please, insert your desire length ? : "))
# counter = 1
# my_list = []
# # Create a program that prints a list of multiples of the number until the list length
# # reaches length.
# while counter <= lnth:
#     my_list.append(num * counter)
#     counter = counter + 1
# print(my_list)

# Challenge 2
# Write a program that asks a string to the user, and display a new string
# with any duplicate consecutive letters removed.
user_word = input("Insert any word you want with double letters: ")
user_word_after = ''
for i, char in enumerate(user_word):
    if user_word[i] == user_word[i-1]:
        continue
    else:
        user_word_after = user_word_after + char
print(user_word_after)