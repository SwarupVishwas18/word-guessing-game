from random import randint
from colorama import Fore,Back
from normal import *
# All Variables!!!

rules = """
=========================================
        RULES OF GAME

1. We need to guess the word.
2. Put position and letter.
3. You have 3 Chances.

=========================================
"""
options = ["animals", "fruits", "anime","colors","flowers"]
wrongAns = 0

given = []


# METHODS..!!

def addWord():
    print(Fore.CYAN)
    print(f"""
    
    1. Add {options[0]}
    2. Add {options[1]}
    3. Add Naruto Characters
    4. Add {options[3]}
    5. Add {options[4]}""")

    try:
        cat = int(input("Enter your choice : "))
    except:
        print(Fore.RED)
        print("Sorry But It must Number Associated!!")
        return None
    filename = options[cat-1]
    file = open(filename+".txt", 'a')

    print(Fore.CYAN)
    print("Enter Words : ")
    print(Fore.MAGENTA)
    print("NOTE : After Completing Your Word Insertion enter" , Fore.LIGHTGREEN_EX , "'wqz'", Fore.MAGENTA," as word.")
    print(Fore.CYAN)
    word = ""

    while True:
        print(Fore.CYAN)
        word = input("Enter the word : ").title()
        if word == 'wqz'.title():
            print(Fore.LIGHTGREEN_EX)
            print("Process Completed Succesfully..!!")
            file.close()
            break
        file.write(word+"\n")
        print(Fore.LIGHTGREEN_EX)
        print("Word Added Successfully..!!")
    

def printUnders():
    for i in given:
        print(i,end=" ")
    print()

def printLines():
    print(Fore.CYAN)
    print("------------------------------")
    print("------------------------------")

def printMenu():
    print(f"""
        1. By {options[0]}
        2. By {options[1]}
        3. By Naruto Characters
        4. By {options[3]}
        5. By {options[4]}
        6. Add Words
        7. Read Rules
        8. About Me
        9. Quit
    """)

def wordFinder(option):
    f = open(options[option]+".txt",'r')
    data = f.readlines()
    return data[randint(0, len(data)-1)].upper().strip()



while True:
    printBrand("Guess Word")
    printMenu()

    try:
        ch = int(input("Enter Your Choice : "))
    except:
        print(Fore.RED)
        print("Input Must Be Numerical..!!")
        continue
    if(ch==9):
        quitMe()
    elif ch == 8:
        aboutMe()
    elif ch == 6:
        addWord()
    elif(ch==7):
        print(Fore.YELLOW)
        print(rules)
    elif(ch>4):
        print(Fore.RED)
        print("Wrong Choice!")
    else:
        word = wordFinder(ch-1)
        length = len(word)

        for i in range(len(word)):
            given.append("_")

        printUnders()

        while True:
            printLines()
            ind = int(input("Enter Position : "))
            letter = input("Enter Letter : ").upper()

            if(word[ind-1]==letter):
                print(Fore.GREEN)
                print("Correct")
                given[ind-1] = letter
                length-=1
            else:
                print(Fore.RED)
                print("Wrong!! Correct Letter is : ",word[ind-1])
                given[ind-1] = word[ind-1]
                wrongAns+=1
                length-=1
            if(wrongAns==3):
                print(Fore.RED)
                print("You Lost !!")
                print("Complete Word : ")
                print(word.upper())
                given.clear()
                
                break
            elif(length==0):
                print(Fore.GREEN)
                print("You Won!!")
                print("Complete Word : ")
                printUnders()
                given.clear()
                
                break
                

            printUnders()