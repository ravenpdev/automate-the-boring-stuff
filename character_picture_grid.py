def printList(data: list[list[str]]) -> None:
    for val in data:
        print(val, sep=", ")


def main() -> None:
    grid = [
        [".", ".", ".", ".", ".", "."],
        [".", "O", "O", ".", ".", "."],
        ["O", "O", "O", "O", ".", "."],
        ["O", "O", "O", "O", "O", "."],
        [".", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "."],
        ["O", "O", "O", "O", ".", "."],
        [".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
    ]

    newGrid: list[list[str]] = [[] for _ in range(6)]
    for x in range(6):
        for y in range(len(grid) - 1):
            newGrid[x].append(grid[y][x])

    printList(newGrid)


if __name__ == "__main__":
    main()
