class Character():
    def __init__(self, name, life = 20, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack
    def basic_attack(self, my_inst):
        x = my_inst.attack - self.life
        return f"Your character's life is {abs(x)}"

class Druid(Character):
    def __init__(self,  name, life, attack):
        super().__init__(name, life, attack)
    def meditate(self):
        return self.life + 10, self.attack - 2
    def animal_help(self):
        return self.attack + 5
    def fight(self, other_inst):
        return other_inst.life - (0.75 * self.life + 0.75 * self.attack)
class Warrior(Character):
    def __init__(self,  name, life, attack):
        super().__init__(name, life, attack)
    def brawl(self, other_inst):
        return (self.attack * 2) - other_inst.life, self.life + (0.5 * self.attack)

    def train(self):
        return self.attack * 2, self.life * 2

    def roar(self, other_inst):
        return other_inst.attack - 3
class Mage(Character):
    def __init__(self,  name, life, attack):
        super().__init__(name, life, attack)

    def roar(self, other_inst):
        return other_inst.attack - 2
    def summon(self):
        return self.attack + 3
    def cast_spell(self, other_inst):
        return  other_inst.life - (other_inst.attack / other_inst.life)





my_inst0 = Character('Leo', 25, 20)
my_inst1 = Character('Oel')
druid = Druid('Dru', 40, 20)
warrior = Warrior('War', 30, 12)
print(druid.meditate())
print(druid.animal_help())
print(druid.fight(my_inst0))
print(warrior.brawl(druid))
print(warrior.train())



