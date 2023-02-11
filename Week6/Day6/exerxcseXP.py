# Exercise 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# united_list_zip = zip(keys, values)
# united_list = list(united_list_zip)
#
# my_dict = {}
#
# for ind, val in enumerate(united_list):
#    my_dict[united_list[ind][0]] = united_list[ind][1]
# print(my_dict)

# Exercise 2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# cost = 0
# for ind, val in enumerate(family):
#     if family.get(val) <= 3 and family.get(val) > 0:
#         print("The ticket is free")
#     elif 3 < family.get(val) < 12:
#         print("The ticket is 10$")
#         cost = cost + 10
#     elif 100 > family.get(val) > 12:
#         print("The ticket is 15$")
#         cost = cost + 15
#     else:
#         break
# print(cost)

# Exercise 3: Zara

# brand = {
#     "name": 'Zara',
#     "creation_date": 1975,
#     "creator_name": ['Amancio', 'Ortega', 'Gaona'],
#     "type_of_clothes": ['men', 'women', 'children', 'home'],
#     "international_competitors": ['Gap', 'H&M', 'Benetton'],
#     "number_stores": 7000,
#     "major_color": [('France', 'blue'), ('Spain', 'red'), ('US', 'pink', 'green')]
# }

# name01 = brand["name"]
# print(f"{name01}'s clients it's millions of people all over the world")
# brand["country_creation"] = 'Spain'
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(brand["major_color"][-1])
# print(len(brand))
# keys_list = list(brand.keys())
# print(keys_list)
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
# new_zara_dict = brand.copy()
# for ind, val in more_on_zara.items():
#     new_zara_dict[ind] = valnu
# #     number_stores - value changed to 10000
# print(new_zara_dict)

# Exercise 4 : Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
users_dict = {}

# for i in range(len(users)):
#     users_dict[users[i]] = i

# for i in range(len(users)):
#     users_dict[i] = users[i]

users.sort()

# for i in range(len(users)):
#     users_dict[users[i]] = i

# for i in range(len(users)):
#     for x in users[i]:
#         if x == 'i':
#             users_dict[users[i]] = i

for i in range(len(users)):
    print(users[i][0])
    if users[i][0] == 'M' or users[i][0] == 'P':
        users_dict[users[i]] = i

print(users_dict)

