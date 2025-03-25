import random


def displayBoard(board: dict[str, dict[str, str]]) -> None:
    for k in board.keys():
        print("|", end="")
        for v in board[k].values():
            print(f" {v} ", end="|")
        print()


def displayTheBoard(board: dict[str, str]) -> None:
    print(f"{board['tl']}|{board['tm']}|{board['tr']}")
    print("-+-+-")
    print(f"{board['ml']}|{board['mm']}|{board['mr']}")
    print("-+-+-")
    print(f"{board['bl']}|{board['bm']}|{board['br']}")


def checkWinner(theBoard: dict[str, str]) -> str:
    winner = ""
    if (
        (theBoard["tl"] == "X" and theBoard["tm"] == "X" and theBoard["tr"] == "X")
        or (theBoard["ml"] == "X" and theBoard["mm"] == "X" and theBoard["mr"] == "X")
        or (theBoard["bl"] == "X" and theBoard["bm"] == "X" and theBoard["br"] == "X")
        or (theBoard["tl"] == "X" and theBoard["ml"] == "X" and theBoard["bl"] == "X")
        or (theBoard["tm"] == "X" and theBoard["mm"] == "X" and theBoard["bm"] == "X")
        or (theBoard["tr"] == "X" and theBoard["mr"] == "X" and theBoard["br"] == "X")
        or (theBoard["tl"] == "X" and theBoard["mm"] == "X" and theBoard["br"] == "X")
        or (theBoard["tr"] == "X" and theBoard["mm"] == "X" and theBoard["bl"] == "X")
    ):
        winner = "player1"

    if (
        (theBoard["tl"] == "O" and theBoard["tm"] == "O" and theBoard["tr"] == "O")
        or (theBoard["ml"] == "O" and theBoard["mm"] == "O" and theBoard["mr"] == "O")
        or (theBoard["bl"] == "O" and theBoard["bm"] == "O" and theBoard["br"] == "O")
        or (theBoard["tl"] == "O" and theBoard["ml"] == "O" and theBoard["bl"] == "O")
        or (theBoard["tm"] == "O" and theBoard["mm"] == "O" and theBoard["bm"] == "O")
        or (theBoard["tr"] == "O" and theBoard["mr"] == "O" and theBoard["br"] == "O")
        or (theBoard["tl"] == "O" and theBoard["mm"] == "O" and theBoard["br"] == "O")
        or (theBoard["tr"] == "O" and theBoard["mm"] == "O" and theBoard["bl"] == "O")
    ):
        winner = "player2"

    return winner


def main():
    print(
        "tl: top-left, tm: top-mid, tr: top-right, ml: mid-left, mm: mid-mid, mr: mid-right",
        "bl: bot-left, bm: bot-mid, br: bot-right",
    )

    # board: dict[str, dict[str, str]] = {
    #     "t": {"l": "-", "m": "-", "r": "-"},
    #     "m": {"l": "-", "m": "-", "r": "-"},
    #     "b": {"l": "-", "m": "-", "r": "-"},
    # }

    theBoard = {
        "tl": " ",
        "tm": " ",
        "tr": " ",
        "ml": " ",
        "mm": " ",
        "mr": " ",
        "bl": " ",
        "bm": " ",
        "br": " ",
    }

    availableMove = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]

    # displayBoard(board)
    displayTheBoard(theBoard)

    symbol = "X"
    winner = ""

    while True:
        print(availableMove)

        userMove = input("enter location move: ")

        if userMove == "":
            break

        if userMove not in theBoard.keys():
            print("Invalid move")
            continue

        theBoard[userMove] = symbol
        availableMove.remove(userMove)
        symbol = "O"

        winner = checkWinner(theBoard)
        if winner != "":
            break

        computerMove = random.choice(availableMove)
        theBoard[computerMove] = symbol
        availableMove.remove(computerMove)
        symbol = "X"

        displayTheBoard(theBoard)

        winner = checkWinner(theBoard)
        if winner != "":
            break

    displayTheBoard(theBoard)
    if winner == "player1":
        print("Player 1 win")
    elif winner == "player2":
        print("Player 2 win")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
