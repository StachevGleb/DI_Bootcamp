# Exercise 1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# all_cats = [Bengal('Bengal', 2), Chartreux('Chartreux', 3), Siamese('Siamese', 4)]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

# Exercise 2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f'{self.name} is barking')
    def run_speed(self):
        speed = self.weight * self.age * 10
        print(f'{self.name} is running with {speed} km/h speed')
        return speed

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f'{self.name} is winner')
        else:
            print(f'{other_dog.name} is winner')


diggy = Dog("Diggy", 2, 20)
other_dog = Dog("Hamood", 1, 10)
other_dog.fight(diggy)





