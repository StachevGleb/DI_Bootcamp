# Exercise 1 
a = 'Hello World\n' * 4
print(a)
 
# Exercise 2 (99^3)*8
x = (99**3)*8
print(x)

# Exercise 3
# >>> 5 < 3 - false
c = 5 < 3
print(c)
# >>> 3 == 3 - true
d = 3 == 3
print(d)
# >>> 3 == "3" - false
f = 3 == "3"
print(f)
# >>> "3" > 3 - false ?
# j = "3" > 3
# print(j)
# >>> "Hello" == "hello" - false
h = "Hello" == "hello"
print(h)

# Exercise 4
computer_brand = 'Asus'
my_str = f"I have a {computer_brand} computer"
print(my_str)

# Exercise 5
name = 'Gleb'
age = '30'
shoe_size = '42'
info = f"My name is {name} and I'am {age} years old. I'm wearing {shoe_size} size shoes."
print(info)

# Exercise 6
a = 2
b = 1
if a > b:
    print('Hello World')

# Exercise 7
# number = int(input("Enter any number to test whether it is odd or even: "))
# if (number % 2) == 0:
#     print ("The number is even")
# else:
#     print ("The provided number is odd")

# Exercise 8
# user_name = input("What is your name?: ")
# if user_name == "Gleb":
#     print("Maybe we are brothers ? Could be ..")
# else:
#     print("This is not my name")

# Exercise 9
value_height = int(input("Your height friend in inches, please: "))
if (value_height*2.54) > 145:
    print ("You are tall enough to ride")
else:
    print ("You need to grow some more to ride")


