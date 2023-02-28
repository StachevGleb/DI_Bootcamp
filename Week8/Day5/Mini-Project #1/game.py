import random
class Game():
    def get_user_item(self):
        user_item = input("Select (r)ock, / (p)aper or (s)cissors:  ")
        checker = True
        while checker:
            if user_item in ['r', 'p', 's']:
                 checker = False
                 return user_item
            else: # it's redundant, please remove because we are doing return one line before
                user_item = input("Select correct letter in () - (r)ock, / (p)aper or (s)cissors:  ")

    def get_computer_item(self):
        comp_item = ["r", "p", "s"]
        return random.choice(comp_item)
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        if user_item == 'r' and computer_item == 'p': 
            return 'loss'
        if user_item == 'r' and computer_item == 's':
            return 'win'
        if user_item == 'p' and computer_item == 's':
            return 'loss'
        if user_item == 'p' and computer_item == 'r':
            return 'win'
        if user_item == 's' and computer_item == 'r':
            return 'loss'
        if user_item == 's' and computer_item == 'p':
            return 'win'
    def play(self):
        user_item = self.get_user_item()
        comp_item = self.get_computer_item()
        res = self.get_game_result(user_item, comp_item)
        val_dict = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        res_dict = {'win': 'You win!', 'loss': 'You lose', 'draw': 'You drew!'}
        print(f'You selected {val_dict[user_item]}. The computer selected {val_dict[comp_item]}. {res_dict[res]}')
        return res



