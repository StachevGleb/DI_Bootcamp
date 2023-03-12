# Exercise 2
import random

# user_num = input("Insert number from 0 to 100: ")
# random_num = random. randint(0, 100)
# print(user_num)
# print(random_num)
# if user_num == random_num:
#     print("It's the same number")
# else:
#     print("It's the wrong number")

# Exercise 3
# import random
# import string
#
# fr_part = random.choices(string.ascii_lowercase, k=2)
# scd_part = random.choices(string.ascii_uppercase, k=3)
# my_str_list = fr_part + scd_part
# my_str = ''.join(my_str_list)
# print(my_str)

# Exercise 4
# from datetime import datetime
#
# now = datetime.now()
# print("now =", now)

# Exercise 5
# from datetime import datetime
# frst_of_NY = datetime(2024, 1, 1, 0, 0, 0)
# now = datetime.now()
# duration = now - frst_of_NY
# print(duration)

# Exercise 6
# from datetime import datetime
#
# now = datetime.now()
#
# def get_birthday():
#     """Get the birthday, catch if it is not a valid date and ask again"""
#     while True:
#         birthdate = input("Enter your date of birth (mm-dd-yyyy): ")
#         try:
#             import datetime
#             return datetime.datetime.strptime(birthdate, "%m-%d-%Y")
#         except ValueError:
#             print(f"'{birthdate}' is not a valid date, try again")
#
# birth_date = get_birthday()
# print(birth_date)
#
# duration = now - birth_date
# print(duration.days*24*60)

# Exercise 7
# from datetime import datetime
# def calcTimeToNextHoliday():
#     now = datetime.now()
#
#     holid_list = [
#         ["Passover", "2023-04-09"],
#         ["Shavuot", "2023-05-25"],
#         ["New year", "2024-01-01"]
#     ]
#
#     holid_date_list = holid_list[0][1].split('-')
#
#     if int(holid_date_list[1]) > now.month:
#         next_holid = datetime(int(holid_date_list[0]), int(holid_date_list[1]), int(holid_date_list[2]), 0, 0, 0)
#         duration = next_holid - now
#         print(f"The next holiday is in {duration}")
#
# calcTimeToNextHoliday()

# Exercise 8
# import orbitalPerPlan as o
#
# def ageOnPlanets():
#     age = input("Tell us your age in seconds, please in Earth years: ")
#     age = int(age)
#     print(f"On Earth {age/o.earth_orb_per} years old")
#     print(f"On Mercury {age/o.mercury_orb_per} years old")
#     print(f"On Venus {age/o.venus_orb_per} years old")
#     print(f"On Mars {age/o.mars_orb_per} years old")
#     print(f"On Jupiter {age/o.jupiter_orb_per} years old")
#     print(f"On Saturn {age/o.saturn_orb_per} years old")
#     print(f"On Uranus {age/o.uranus_orb_per} years old")
#     print(f"On Neptune {age/o.neptune_orb_per} years old")
# ageOnPlanets()

# Exercise 9
import faker

users = []
def users_fake_list():
    input('Your name: ')
    input('Your address: ')
    input('Your language code : ')
    users.append({'name': faker.Faker().name()})
    users.append({'address': faker.Faker().address()})
    users.append({'language code': faker.Faker().language_code()})


users_fake_list()
print(users)
