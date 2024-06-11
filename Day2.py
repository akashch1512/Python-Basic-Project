def akash():
    print("hehehehehe You are such a stupid person ! now you entered into my house ! now no one can save you!")
    print("run(1) else figth(0)")
    choice=int(input())
    os.system("cls")
    if(choice==1):
        print("HA HA HA You Cant defect me ! or either run now you all are died ! ")
        print("YOU LOST")
    if(choice==0):
        print("ahhhhhhhhhhhhhhhhhhhh Your spirt defected me ! you never lose hope hence Won ! and this is the Truth of life ! you can never fail if you try continuously")
import os
import time
os.system("cls")
print("""\nHello Explorer ! Its Akash from the Future itself.... \nWelcome to The Story Game ! 
      Are you ready to play?? \nOhh! But Before we Start What's Your Name Buddy?? """)
user_name=input("-->")
print(f"\nNice Name '{user_name} The Explorer' Now lets starts the Game !!")
print("ya ik scrren is messy rigth?? let me clear it! in next 3 sec!")
for i in range(1,4):
    time.sleep(3)
    print(f"{i} ",end="")
time.sleep(3)
os.system("cls")
print(f"Here the Actual Game Begins {user_name}")
print("3 of yours friends goes to horror banglo near your home !\nchoose if you want to stay home (1) or horror banglo (0)")
choice=int(input())
os.system("cls")
if(choice==1):
    print(f"Why are you afrid of that horror banglo ! dont you know ?? that ghosts does not exits! take a chill pill {user_name}")
    print("now you wanna go home?(1) or go to horror banglo (0) with friends!")
    choice=int(input())
    os.system("cls")
    if(choice==0):
        akash()
    if(choice==1):
        print("you such a looser You loose the game and the fun itself")
if(choice==0):
    akash()







    """
    The code you provided is a good start for a password generator in Python. Here are some improvements you can make:
 * Stronger password generation: While it includes a variety of character types, it doesn't ensure the password meets recommended complexity requirements. Consider using the random.sample() function to select characters from each category (uppercase letters, lowercase letters, numbers, symbols) and ensure at least one character from each category is included in the final password.
 * Error handling: It includes some error handling, but you could add more to make it more robust. For example, you could handle cases where the user enters a non-numeric value for the password length.
 * User-friendliness: Consider adding more options to customize the password generation process. For instance, allow users to specify the number of characters from each category (uppercase letters, lowercase letters, numbers, symbols).
Here are some resources that can help you improve your password generator:
 * Python's random module: https://python.readthedocs.io/en/stable/library/random.html
 * Password strength recommendations: https://pages.nist.gov/800-63-3/sp800-63b.html

    
    """