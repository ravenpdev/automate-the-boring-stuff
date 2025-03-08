import time


def addNameUsingConcatenate(haystack: list[str], needle: str) -> list[str]:
    start = time.perf_counter()
    haystack = haystack + [needle]
    end = time.perf_counter()

    print((end - start) * 1000)

    return haystack


def addNameUsingAppend(haystack: list[str], needle: str) -> None:
    start = time.perf_counter()
    haystack.append(needle)
    end = time.perf_counter()

    print((end - start) * 1000)


def main() -> None:
    catNames: list[str] = []

    while True:
        name = input("Enter cat name: ")

        if name == "":
            break

        # catNames = catNames + [name]
        # addNameUsingAppend(catNames, name)
        catNames = addNameUsingConcatenate(catNames, name)

    for name in catNames:
        print(name)


if __name__ == "__main__":
    main()
