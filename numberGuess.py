#           Guess the Number
#   This program will generate a number from 0-100.
#   The program will then ask the user for a number from 0-100.
#   It will display “Greater than” if the inputed number is greater than the random number.
#   It will also display “Less than” if the inputed number is greater than the random number.
#   The user can keep guessing until the random number has been guessed correctly.

from random import randint

def userPlay():
    randNum = randint(0,100)
    userGuessing = True

    while userGuessing:
        userNum = int(input("Guess the number (0-100): "))
        if userNum == randNum:
            print(f"You guessed it! The number is {randNum}!")
            userGuessing = False
        else:
            if userNum > randNum:
                print("Your number is GREATER THAN the random number!\n")
            else:
                print("Your number is LESS THAN the random number!\n")
userPlay()
userAsk = True
while userAsk == True:
    tryAgain = str(input("Keep playing?(Y/N): ")).lower()
    if tryAgain == "y":
        print("\nGet ready for the next game!")
        userPlay()
    else:
        print("Thank you for playing!")
        userAsk = False
        exit