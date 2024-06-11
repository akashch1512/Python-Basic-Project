# Password Genrator
def Password_Genrator():
    print("Welcome To Password Genrator By Akash".center(100).upper())
    print("Enter The Length Of Password You Want!")
    try:
        Length=int(input("-->"))
        if(Length==0):
            print("\nDid you out a wrong input?? Try again !")
            Password_Genrator()
            exit
        Charectors={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*'}
        Password=""
        for k,i in enumerate(Charectors):
            Password=Password+i
            if(Length==k+1):
                break
        print(f"Your Password is {Password} \nThanks For Using My Software!\n")
        print("Enter 1 If want to use again else enter anything")
        Length=int(input("-->"))
        if(Length==1):
            Password_Genrator()
        else:
            exit
    except:
        print("Enter a vaild number please!")
        Password_Genrator()
Password_Genrator()






"""


The code you provided is a good start for a password generator in Python. Here are some improvements you can make:
 * Stronger password generation: While it includes a variety of character types, it doesn't ensure the password meets recommended complexity requirements. Consider using the random.sample() function to select characters from each category (uppercase letters, lowercase letters, numbers, symbols) and ensure at least one character from each category is included in the final password.
 * Error handling: It includes some error handling, but you could add more to make it more robust. For example, you could handle cases where the user enters a non-numeric value for the password length.
 * User-friendliness: Consider adding more options to customize the password generation process. For instance, allow users to specify the number of characters from each category (uppercase letters, lowercase letters, numbers, symbols).
Here are some resources that can help you improve your password generator:
 * Python's random module: https://python.readthedocs.io/en/stable/library/random.html
 * Password strength recommendations: https://pages.nist.gov/800-63-3/sp800-63b.html



"""
pUxJnWvkmQ4Dfs0g%eXiPw1oV82R#YArtGO!LIh&^qT73CHjlM5Kd$bcFuzZByaNE6*S@9