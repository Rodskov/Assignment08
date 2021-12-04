#               Lottery Winner
#   This program will ask 3 numbers from the user.
#   It will then generate 3 random winning numbers.
#   It will then display "Winner" if the numbers match.
#   The program will also ask if the user wants to play again.

from random import randint

def userAsk():
    firstNum = int(input("Enter your first number (0-9): "))
    secondNum = int(input("Enter your second number (0-9): "))
    thirdNum = int(input("Enter your third number (0-9): "))
    return firstNum, secondNum, thirdNum

playProgram = "y"

while playProgram[0] == "y":
    firUserNum, secUserNum, thiUserNum = userAsk()
    userNumList = [firUserNum, secUserNum, thiUserNum]
    firRandNum = randint(0,9)
    secRandNum = randint(0,9)
    thiRandNum = randint(0,9)
    randNumList = [firRandNum, secRandNum, thiRandNum]
    if all(i in randNumList for i in userNumList):
        print("Winner!")
    else:
        print("You lost...")
    print(f"Winning Numbers: {firRandNum}, {secRandNum}, {thiRandNum}")
    playProgram = str(input("Try again? (Y/N): ")).lower()
    if playProgram == "y":
        print("\nNext round!")
    else:
        print("\nThank you for playing!")
        exit