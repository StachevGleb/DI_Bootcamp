from game import Game
def get_user_menu_choice():
    print("Menu:")
    print("(g) Play a new game:  ")
    print("(x) Show scores and exit:  ")
    user_menu_choice = input(": ")
    checker = True
    while checker:
        if user_menu_choice == 'x':
            pass
        elif user_menu_choice == 'g':
            test = Game()
            res = test.play()
            print(print_results(res))
            res[res] += 1
        else:
            print("Menu:")
            print("(g) Play a new game:  ")
            print("(x) Show scores and exit:  ")
            user_menu_choice = input(": ")
def print_results(res):
    print("Results:")
    print(f'Winner - {res["win"]} times, Looser - {res["loss"]} times, Drews - {res["draw"]} times')

def main():
    get_user_menu_choice()



main()

