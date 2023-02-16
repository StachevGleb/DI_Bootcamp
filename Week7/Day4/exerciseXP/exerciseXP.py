# import random
# tempr = 0
# def get_random_temp(season):
#     if season == "summer":
#         rand_val = random.randint(22, 40)
#     elif season == "autumn":
#         rand_val = random.randint(16, 35)
#     elif season == "winter":
#         rand_val = random.randint(-10, 10)
#     elif season == "spring":
#         rand_val = random.randint(12, 32)
#     else:
#         print("We have no season like that on this planet")
#     return rand_val
#
# def main():
#     season = input("Tell us your current season: ")
#     rand_value = get_random_temp(season)
#     if rand_value < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 < rand_value <= 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 17 < rand_value <= 23:
#         print("Quite chilly! Only in the morning")
#     elif 24 < rand_value <= 32:
#         print("Perfect weather to running")
#     elif 33 < rand_value <= 40:
#         print("Really hot")
#     print(f"The temperature right now is {rand_value} degrees Celsius")
# main()

# Exercise 2

# date_of_birth = input("Please insert your birthday in follow format (yyyy/mm/dd): ")
# gender = input("Insert your gender 'm' or 'f' ? :")


# def get_age(year, month, day):
#     current_date = ['2023', '02', '16']
#     age = int(current_date[0]) - int(year)
#     return age
#
# def can_retire(gender, date_of_birth):
#     date_of_birth_list = date_of_birth.split("/")
#     year_of_birth = date_of_birth_list[0]
#     month_of_birth = date_of_birth_list[1]
#     day_of_birth = date_of_birth_list[2]
#     age = get_age(year_of_birth, month_of_birth, day_of_birth)
#     if gender == "m" and age > 67:
#         print("You can retire")
#     elif gender == "f" and age > 62:
#         print("You can retire")
#     else:
#         print("You can't retire")
# can_retire(gender, date_of_birth)

# Exercise 3
num = input("Please indert number between 0 and 10:")
def num_adder(num):
    x = ''
    sum = 0
    str_num_list = []
    for i in range(4):
        x = x + num
        str_num_list.append(x)
        print(str_num_list)
    for el in str_num_list:
        sum = sum + int(el)
    print(sum)

num_adder(num)