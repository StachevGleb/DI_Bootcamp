# my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
# res = 0
# def addition_list():
#     try:
#         for item in my_list:
#             res += item
#     except:
#         print('You have not integer item')
# print(res)
#
# addition_list()

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
new_peop = list(filter(lambda s: len(s) <= 4, people))
print(list(map(lambda s: s + " Hello you there", new_peop)))