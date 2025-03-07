import random
import sys


def getUserMove() -> str:
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        userMove = input()
        if userMove == "r":
            print("ROCK versus...")
            break
        elif userMove == "p":
            print("PAPER versus...")
            break
        elif userMove == "s":
            print("SCISSORS versus...")
            break
        elif userMove == "q":
            sys.exit()
        else:
            print("Type one of r, p, s, or q.")
            continue

    return userMove


def getComputerMove() -> str:
    randomNumber = random.randint(1, 3)
    computerMove = ""
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    return computerMove


def checkResult(userMove: str, computerMove: str, result: list[int]) -> None:
    if userMove == computerMove:
        print("It is a tie!")
        result[2] = result[2] + 1
    elif (
        (userMove == "s" and computerMove == "p")
        or (userMove == "p" and computerMove == "r")
        or (userMove == "r" and computerMove == "s")
    ):
        print("You win!")
        result[0] = result[0] + 1
    else:
        print("You loss!")
        result[1] = result[1] + 1


def rockPaperScissors() -> None:
    print("ROCK, PAPER, SCISSORS")

    result = [0, 0, 0]

    print(f"{result[0]} Wins, {result[1]} Losses, {result[2]} Ties")

    while True:
        userMove = getUserMove()

        computerMove = getComputerMove()

        checkResult(userMove, computerMove, result)

        print(f"{result[0]} Wins, {result[1]} Losses, {result[2]} Ties")


if __name__ == "__main__":
    rockPaperScissors()
