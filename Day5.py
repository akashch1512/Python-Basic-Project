import os
import pygame
import threading

def Display_Files(Path):
    Objects=os.listdir(os.path.join(Path))
    print("\nThe Location Have These Listed Files : ")
    for i,k in enumerate(Objects):
        print(f"\n{i}) {k}")

def Play_Sound(new_path , stopped):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(new_path))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)
    stopped.wait()
    pygame.mixer.music.stop()

def welcome():
    os.system("cls")
    print("\t!i!i!i!i!i!i!i!i!i!i!i!i * WELCOME * i!i!i!i!i!i!i!i!i!i!i!i!i!i\n".expandtabs(tabsize=30))

welcome()

Path=input("Please Enter The Path Of The File You Stored The Songs! if you dont have a file press 0 : ") # Display File Path

if Path=="0":
    Path="song"
    
Display_Files(os.path.join(Path))
index_input=int(input("\nEnter The Number of the file you want to open : ".title()))
file=(os.listdir(Path))[index_input]
new_path= rf"{Path}\{file}"

stopped=threading.Event()
t=threading.Thread(target=Play_Sound,args=(new_path, stopped))
t.start()    
input("\npress enter to stop the music : ".title())
print("haha You are rick rolled ! You cant stop it !!!")
Play_Sound(new_path, stopped)
stopped.set()
t.join()
