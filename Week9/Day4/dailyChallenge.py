class Person():
    def __init__(self, name, list_foods_like, list_foods_hate):
        self.name = name
        self.list_foods_like = list_foods_like
        self.list_foods_hate = list_foods_hate
    def taste(self, food_name):
        if food_name in self.list_foods_like:
             print(f"{self.name} eats the {food_name} and loves it!")
        elif food_name in self.list_foods_hate:
             print(f"{self.name} eats the {food_name} and hates it!")
        else:
             print(f"{self.name} eats the {food_name} !")

p1 = Person("Sam", ["ice cream"], ["carrots"])

p1.taste("ice cream")
p1.taste("cheese")
p1.taste("carrots")