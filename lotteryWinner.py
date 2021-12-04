#               Lottery Winner
#   This program will ask 3 numbers from the user.
#   It will then generate 3 random winning numbers.
#   It will then display "Winner" if the numbers match.
#   The program will also ask if the user wants to play again.

from random import randint

def userAsk():
    firstNum = int(input("Enter your first number: "))
    secondNum = int(input("Enter your second number: "))
    thirdNum = int(input("Enter your third number: "))
    return firstNum, secondNum, thirdNum

firUserNum, secUserNum, thiUserNum = userAsk()
firRandNum = randint(0,9)
secRandNum = randint(0,9)
thiRandNum = randint(0,9)
randNumList = [firRandNum, secRandNum, thiRandNum]

playProgram = "y"

print(firRandNum, secRandNum, thiRandNum)