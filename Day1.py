# Game to cheak if a given number is correct or not
import random

print("Welcome to Guess Game...!!".center(100))

list1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
guess_num=random.choice(list1)

while True:

    print("Enter any number between 0 To 20")
    num=int(input())
    
    if(guess_num==num):
        print("You Got me !")
        break

    elif (guess_num<num):
        print("You Choose a Larger number !")

    else:
        print("Choice is smaller !")








"""The code you've written looks like a good start for a guessing game! Here are some ways you can improve it:
 * Add more complexity:  You can make the game more challenging by increasing the number range or allowing a limited number of guesses.
 * Provide hints:  Instead of just saying "higher" or "lower," you could give the user a hint about how close their guess is to the target number.
 * Keep score: Track the number of guesses it takes the user to find the correct number and keep a high score.
"""