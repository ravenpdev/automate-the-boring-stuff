def printTitle(title: str) -> None:
    print("\n")
    asterisk = "*" * 5
    title = asterisk + f" {title} " + asterisk
    print(title)


def operators() -> None:
    printTitle("Operators")
    print("Exponent", 2**3)
    print("Modulus/remainder", 22 % 8)
    print("Integer division", 22 // 8)
    print("Division", 22 / 8)
    print("Multiplication", 3 * 5)
    print("Subtraction", 5 - 2)
    print("Addition", 2 + 2)


def dataTypes() -> None:
    printTitle("Data types")
    # Integers -2, -1, 0, 1, 2, 3, 4, 5
    # Floating-point numbers -1.25, -1.0, 0.5, 0.0, 0.5, 1.0, 1.25
    # Stringgs 'a', 'aa', 'aaa', 'Hello!', '11 cats'
    my_int = 1
    my_float = 1.0
    my_string = "raven"
    print(my_int)
    print(my_float)
    print(my_string)


def variables() -> None:
    printTitle("Variables")
    spam: int = 40
    print(spam)
    spam = 33
    print(spam)
    currentBalance = 10_000
    print(currentBalance)
    account1 = "raven"
    print(account1)


def firstProgram() -> None:
    name = input("What is your name? ")
    print(f"It is good to meet you, {name}")
    print(f"The length of your name is: {len(name)}")
    age = input("What is your age? ")
    print(f"You will be {int(age) + 1} in a year.")


def main() -> None:
    print("Hello from automateboringstaff!")

    operators()

    dataTypes()

    variables()

    firstProgram()


if __name__ == "__main__":
    main()
