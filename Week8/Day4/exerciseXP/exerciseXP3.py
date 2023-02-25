# Exercise 3

from random import randint
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

class PetDog(Dog):
    def __init__(self, name, age, weight,  trained = False):
        self.trained = trained
        super().__init__(name, age, weight)

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dog_list = [self.name]
        for dog in args:
            dog_list.append(dog.name)
        playing_dogs = ", ".join(dog_list)
        print(f'{playing_dogs} all play together')

    def do_a_trick(self):
        list_of_actions = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
        if self.trained:
            print(f'{self.name} {list_of_actions[randint(0, 3)]}')

diggy = Dog("Diggy", 2, 20)
other_dog = Dog("Hamood", 1, 10)
other_dog.fight(diggy)
pet_dog1 = PetDog("Rex", 3, 3, True)
pet_dog2 = PetDog("Tex", 4, 5)
pet_dog3 = PetDog("Fex", 7, 9)
pet_dog1.train()
pet_dog2.play(pet_dog1, pet_dog3)
# pet_dog3.train()
pet_dog3.do_a_trick()

