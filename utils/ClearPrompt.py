import os

def clear():
    if(os.name == "nt"):
        os.system("cls")
        os.system("cls")
    else:
        os.system("clear")
        os.system("clear")