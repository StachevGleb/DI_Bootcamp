# Exercise 1

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#         print(cat_name, cat_age)
#
# cats_list = []
# cats_list.append(Cat("Cat1", 1))
# cats_list.append(Cat("Cat2", 2))
# cats_list.append(Cat("Cat3", 3))
#
# def oldest_cat():
#     number = 0
#     for cat in cats_list:
#         if cat.age > number:
#             number = cat.age
#             name = cat.name
#     return number, name
#
# oldest_cat_tuple = oldest_cat()
#
# print(f"The oldest cat is {oldest_cat_tuple[1]}, and is {oldest_cat_tuple[0]} years old.”. Use the function previously created")


# Exercise 2

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def bark(self):
#         print(f"{self.name} goes woof!")
#     def jump(self):
#         print(f"{self.name} jumps {self.height} cm high!")
#
# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("Teacup", 20)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()
# if sarahs_dog.height > davids_dog.height:
#     print(f"{sarahs_dog.name} is bigger his height {sarahs_dog.height}")
# else:
#     print(f"{davids_dog.name} is bigger - his height {davids_dog.height}")

# Exercise 3

# lyrics = ["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]
# class Song:
#     def sing_me_a_song(self, lyrics):
#         for i in range(len(lyrics)):
#             print(lyrics[i])
# my_song = Song()
# my_song.sing_me_a_song(lyrics)

# Exercise 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        self.animals.append(new_animal)
    def get_animals(self):
        print(self.animals)
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        print(self.animals)
    def sort_animals(self):
        self.x = sorted(self.animals)
        print(self.x)
    def get_groups(self):
        res = []
        def util_func(x, y):
            return x[0] == y[0]
        for sub in self.x:
            ele = next((y for y in res if util_func(sub, y[0])), [])
            if ele == []:
                res.append(ele)
            ele.append(sub)
        for el in res:
            print(el)

ramat_gan_safari = Zoo("Yafo's_zoo")
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cat_dog')
ramat_gan_safari.add_animal('Tiger')
ramat_gan_safari.add_animal('Wolf')
ramat_gan_safari.add_animal('Dog')
ramat_gan_safari.add_animal('Rabbit')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Tiger')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()