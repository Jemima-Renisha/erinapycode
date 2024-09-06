import random
choices = ['rock', 'paper', 'scissors']

def getcomputerchoice():
    return random.choice(choices)

def playerchoice():
    print("choose rock or paper or scissors")
    playerinput = input("your choice:")
    while playerinput not in choices:
        print("Invalid choice")
        playerinput = input("your choice:")
    return playerinput

def findwinner(playerinput, computerinput):
    if playerinput == computerinput:
        return "it is tie"
    elif (playerinput=="rock" and computerinput=="scissors")or (playerinput=="paper" and computerinput=="rock") or(playerinput=="scissors" and computerinput=="paper"):
        return "you win"
    else:
        return "computer win"

def playgame():
    computerinput = getcomputerchoice()
    playerinput = playerchoice()
    print("computer choice is",computerinput)
    result = findwinner()
    print(result)