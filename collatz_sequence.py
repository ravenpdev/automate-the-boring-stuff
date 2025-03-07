import sys


def collatz(n: int) -> int:
    if n % 2 == 0:
        print(n // 2)
        return n // 2

    print(3 * n + 1)
    return 3 * n + 1


def main() -> None:
    while True:
        try:
            userInput = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input please enter a number")
            continue
        except KeyboardInterrupt:
            sys.exit()

    while True:
        userInput = collatz(userInput)  # 3, # 10

        if userInput == 1:
            break


if __name__ == "__main__":
    main()
