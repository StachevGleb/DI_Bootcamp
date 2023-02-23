class Farm:

    def __init__(self, name):
        self.name = name
        print(f"{name}'s farm")
    def add_animal(self, name, animal_list, quantity = 2):
        print(name, quantity)
        animal_list.append(name)
        print(animal_list)
    def get_info(self):
        print("     E-I-E-I-0!")
    def get_animal_types(self, animal_list):
        sort_add_list = sorted(animal_list)
        sentence = ','.join(sort_add_list)
        animal_list = sort_add_list
        return sentence
    def get_short_info(self, name):
        sentence = macdonald.get_animal_types(animal_list)
        alfa_list = sentence.split(",")
        print(f"{name}’s farm has {alfa_list[0]}, {alfa_list[1]} and {alfa_list[2]}.")




animal_list = []
macdonald = Farm("McDonald")
macdonald.add_animal('cow', animal_list, 5)
macdonald.add_animal('sheep', animal_list)
macdonald.add_animal('sheep', animal_list)
macdonald.add_animal('goat', animal_list, 12)
macdonald.get_animal_types(animal_list)
macdonald.get_short_info("McDonald")
macdonald.get_info()
