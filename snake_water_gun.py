import os
import random
def Game():
    os.system("cls")
    # 0 snake 1 water 2 gun
    math=[[0,1,-1], # 00 01 02
          [-1,0,1], # 10 11 12
          [1,-1,0]] # 20 21 22
    welcome()
    i=int(input("press 0, 1, 2 for snake, water, gun respectivly!\n".title()))
    k=random.choice([0,1,2])
    result= 'Won' if math[i][k]==1 else "Drawn" if math[i][k]==0 else 'Loosen'
    os.system("cls")
    print(f"as 0 --> snake 1 --> water and 2 --> gun!\nComputer choosen {k} and you choose {i} hence the game is {result} by you!".title())

def welcome():
    print("welcome to the game ! snake water and gun press 1 for rules else press 0 to go ahead !".title())
    test=int(input())
    os.system("cls")
    if test == 1:
        os.system("cls")
        print('''--- The rules of the Snake Water and Gun game are as follows ---
* Snake(0) vs. Water(1): Snake drinks the water hence wins.
* Water(1) vs. Gun(2): The gun will drown in water, hence a point for water.
* Gun(2) vs. Snake(0): Gun will kill the snake and win.
* In situations where both players choose the same object, the result will be a draw.''')
        print("\nto start with the game press any key".title())
        input()
        os.system("cls")

if __name__=='__main__':
    Game()