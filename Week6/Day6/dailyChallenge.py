# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# my_str = input('Please, insert any word: ')
# # my_str = 'aaassddff'
# my_list = list(my_str.strip(''))
# my_store_list = []
# my_res_list =  my_list.copy()
# my_dict = {}
# for index, value in enumerate(my_list):
#     if value not in my_store_list:
#         my_store_list.append(value)
#         my_dict[value] = []
# for ind, val in enumerate(my_res_list):
#     if val in my_dict:
#         my_dict.setdefault(val, []).append(ind)
# print(my_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store
# with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
#
# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
#
# wallet = "$300"
#
# ➞ ["Bread", "Fertilizer", "Water"]

my_wallet = 300
list_of_purchases = []

items_purchase = {
  'Water': 1,
  'Bread': 3,
  'TV': 1000,
  'Fertilizer': 20
}

for x in items_purchase:
    if my_wallet >= items_purchase[x]:
        my_wallet = my_wallet-items_purchase[x]
        list_of_purchases.append(x)
    else:
        print('Nothing')
print(list_of_purchases)