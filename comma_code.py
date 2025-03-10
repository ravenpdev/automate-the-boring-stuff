def printLists(data: list[str]) -> None:
    for value in data:
        if data.index(value) == len(data) - 1:
            print(f"and {value}")
        else:
            print(value, end=", ")


def main():
    spam = ["apples", "bananas", "tofu", "cats", "dog"]
    printLists(spam)

    spam: list[str] = []
    printLists(spam)


if __name__ == "__main__":
    main()
