from game import Game
def get_user_menu_choice():
    print("Menu:")
    print("(g) Play a new game:  ")
    print("(x) Show scores and exit:  ")
    user_menu_choice = input(": ")
    checker = True
    result = []
    while checker:
        if user_menu_choice == 'x':
            checker = False
<<<<<<< HEAD
            break
=======
            pass # we use the pass just to define empty function, if, for, etc not to return, so use return or break
>>>>>>> 78dfa3048d952ef3ba4d5e526ec2c17f9a59fa57
        elif user_menu_choice == 'g':
            test = Game()
            res = test.play()
            result.append(res)
            print_results(result)
        else:
            print("Menu:")
            print("(g) Play a new game:  ")
            print("(x) Show scores and exit:  ")
            user_menu_choice = input(": ")
def print_results(result):
    print("Results:")
    print(f'Winner - {result.count("win")} times, Looser - {result.count("loss")} times, Drews - {result.count("draw")} times')
    print(f"Thank you for playing.")
def main():
    get_user_menu_choice()

main()

