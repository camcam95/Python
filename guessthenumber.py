"""
Finished 01/02/23

Author: phylyp
Remake: camcam95

Guess The Number
"""

"""
GameLoop
    + init()
        - game state
    + processInput()
        - controls
    + update()
        - update game state using results of processInput()
    + render()
        - convert game state to visuals
    + run()
        - the "GameLoop"
"""

import random


def init():
    return None, random.randint(1, 10)


def processInput():
    while True:
        word = input("What's the magic number? : \n")
        if word == "quit":
            return None

        try:
            playerNumber = int(word)
            break
        except ValueError:
            print("Please type a number without decimals!")
            continue

    return playerNumber


def update(gameStatus, magicNumber, playerNumber):
    if playerNumber is None:
        gameStatus = "end"
    elif playerNumber == magicNumber:
        gameStatus = "win"
    elif magicNumber < playerNumber:
        gameStatus = "lower"
    elif magicNumber > playerNumber:
        gameStatus = "higher"

    return gameStatus, magicNumber


def render(gameStatus, magicNumber):
    if gameStatus == "win":
        print("This is correct! You win!")
    elif gameStatus == "end":
        print("Bye!")
    elif gameStatus == "lower":
        print("Lower")
    elif gameStatus == "higher":
        print("Higher")
    else:
        raise RuntimeError("Unexpected game status{}".format(gameStatus))


def run():
    gameStatus, magicNumber = init()
    while gameStatus != "win" and gameStatus != "end":
        playerNumber = processInput()
        gameStatus, magicNumber = update(gameStatus, magicNumber, playerNumber)
        render(gameStatus, magicNumber)


run()
