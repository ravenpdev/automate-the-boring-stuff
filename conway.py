import copy
import time


WIDTH = 40
HEIGHT = 12


def printCurrentCell(cell: list[list[str]]) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cell[x][y], end="")
        print()


def main():
    # Create a list of of list for the cells:
    nextCells: list[list[str]] = []
    for x in range(WIDTH):
        column: list[str] = []
        for y in range(HEIGHT):
            # if random.randint(0, 100) % 2 == 0:
            if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):  # glider pattern
                column.append("#")
            else:
                column.append(" ")
        nextCells.append(column)

    while True:
        print("\n\n\n")
        currentCells = copy.deepcopy(nextCells)

        printCurrentCell(currentCells)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get the neighboring coordinates
                # '% WIDTH' ensures left coordinate is always between 0 and WIDTH - 1
                leftCoord = (x - 1) % WIDTH  # index 39
                rightCoord = (x + 1) % WIDTH  # index 1
                aboveCoord = (y - 1) % HEIGHT  # index 11
                belowCoord = (y + 1) % HEIGHT  # index 1

                # Count number of living neighbors:
                numNeighbors = 0
                if currentCells[leftCoord][aboveCoord] == "#":  # 39, 11
                    numNeighbors += 1  # top-left neighbor is alive.
                if currentCells[x][aboveCoord] == "#":
                    numNeighbors += 1  # top neighbor is alive.
                if currentCells[rightCoord][aboveCoord] == "#":
                    numNeighbors += 1  # top-right neighbor is alive
                if currentCells[leftCoord][y] == "#":
                    numNeighbors += 1  #  left neighbor is alive
                if currentCells[rightCoord][y] == "#":
                    numNeighbors += 1  # right neighnor is alive
                if currentCells[leftCoord][belowCoord] == "#":
                    numNeighbors += 1  # bottom-left neighbor is alive
                if currentCells[x][belowCoord] == "#":
                    numNeighbors += 1  # bottom neighbor is alive
                if currentCells[rightCoord][belowCoord] == "#":
                    numNeighbors += 1  # bottom-right neighbor is alive

                # Set cell based on Conway's Game of life rules:
                if currentCells[x][y] == "#" and (
                    numNeighbors == 2 or numNeighbors == 3
                ):
                    nextCells[x][y] = "#"
                elif currentCells[x][y] == " " and numNeighbors == 3:
                    nextCells[x][y] = "#"
                else:
                    nextCells[x][y] = " "

        time.sleep(1)
    # printCurrentCell(nextCells)


if __name__ == "__main__":
    main()
