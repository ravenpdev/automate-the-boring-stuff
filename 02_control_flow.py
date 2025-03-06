import random
import sys


def printTitle(title: str) -> None:
    print("\n")
    asterisk = "*" * 5
    title = asterisk + f" {title} " + asterisk
    print(title)


def booleans() -> None:
    isRunning: bool = True
    print(isRunning)


def comparisonOperators() -> None:
    # Comparison operators, also called relational operators, compare two values and evaluate to a single Boolean value.
    print("42 == 42 ->", 42 == 42)
    print("42 == 99 ->", 42 == 99)
    print("2 != 3 ->", 2 != 3)
    print("2 != 2 ->", 2 != 2)
    print("'hello' == 'hello' ->", "hello" == "hello")
    print("'hello' == 'Hello' ->", "hello" == "Hello")
    print("True == True ->", True is True)
    print("True == False ->", True is False)
    print("42 == 42.0 ->", 42 == 42.0)
    print("42 == '42' ->", 42 == "42")


def booleanOperators() -> None:
    # and, or, not are used to compare Boolean values.

    # binary boolean operators
    # the and and or operator always take two boolean values (or expression), so they are
    # considered binary operators.
    printTitle("and operator")
    print(True and True)
    print(False and True)
    print(False and False)

    printTitle("or operator")
    print(True or True)
    print(False or True)
    print(False or False)

    # Tne not Operator
    # Unline and and or, the not operator operates on only one Boolean value (or expression).
    # This makes it a unary operator.
    printTitle("not operator")
    print(not True)
    print(not not not not True)

    # Mixing boolean and comparison operators
    printTitle("Mixing boolean and comparison operators")
    print((4 < 5) and (5 < 6))
    print((4 < 5) and (9 < 6))
    print((1 == 2) or (2 == 2))

    # The boolean operators have an order of operations just like the math operators do.
    # after any math and comparison operators evaluate. Python evaluates the not operators first,
    # then the and operators, and then the or operators.


def blockOfCodes() -> None:
    name = "Mary"
    password = "swordfish"

    if name != "Mary":
        return

    print("Hello, Mary")

    if password != "swordfish":
        print("Wrong password.")
        return

    print("Access granted.")


def flowControl() -> None:
    name = "Carol"
    age = 3000

    if name == "Alice":
        print("Hi, Alice.")
    elif age < 12:
        print("You are not Alice, kiddo.")
    else:
        print("You are neither Alice nor a little kid.")
    # elif age > 100:
    #     print("You are not Alice, grannie.")
    # elif age > 2000:
    #     print("Unline you, Alicei s not an undead, immortal vampire.")


def whileLoop() -> None:
    count = 0
    while count < 5:
        print("Hello, world.")
        count = count + 1

    # An annoying while loop
    # name = ""
    # while name != "your name":
    #     print("Please type your name.")
    #     name = input()
    # print("Thank you!")

    # Truthy and Falsey values
    # Conditionns will consider some values in other data types equivalent to True and False.
    # When used in conditions, 0, 0.0, andn '' are considered False, while all other values
    # are considered True.
    # name = ""
    # while not name:
    #     print("Enter your name:")
    #     name = input()

    # print("How many guests will you have?")
    # numbOfGuests = int(input())
    # if numbOfGuests:
    #     print("Be sure to have enough room for all your guests.")
    # print("Done")

    while True:
        name = input("Who are you?")

        if name != "Joe":
            continue

        password = input("Hello, Joe. What is the password? (It is a fish.)")

        if password == "swordfish":
            break
    print("Access granted.")


def forLoopsAndRange() -> None:
    print("My name is")
    for i in range(5):
        print(f"Jimmy Five Times ({i})")

    total = 0
    for num in range(101):
        total = total + num
    print(total)

    for i in range(0, 10, 2):
        print(i)

    for i in range(5, -1, -1):
        print(i)


def importingModules() -> None:
    # All python programs can call a basic set of functions called built-in functions, including
    # the print(), input(), and len() functions you've seen before. Pythonn also comes with a
    # set of modules called the standard library. Each module is a python program that contains
    # a related group of functions that can be embedded in your programs.
    # Before you can use the functions in a module, you must import the module with an
    # import statementn. In code, an import statement consists of the following:
    # - The import keyword
    # - The name of the module
    # - Optionally, more module names, as long as they are separated by commas
    for _ in range(5):
        print(random.randint(1, 10))


def systemExit() -> None:
    while True:
        print("Type exit to exit.")
        response = input()
        if response == "exit":
            sys.exit()
        print(f"You typed {response}.")


def guessTheNumber() -> None:
    print("I am thinking of a number between 1 and 20.")
    numToGuess = random.randint(1, 20)
    guessCount = 1

    while True:
        guess = int(input("Take a guess."))

        if guess == numToGuess:
            break

        if guess < numToGuess:
            print("Your guess is too low.")

        if guess > numToGuess:
            print("Your guess is too high")

        guessCount = guessCount + 1

    print(f"Good job! you guessed my number in {guessCount}")


def main() -> None:
    pass
    # booleans()

    # comparisonOperators()

    # booleanOperators()

    # blockOfCodes()

    # flowControl()

    # whileLoop()

    # forLoopsAndRange()

    # importingModules()

    # systemExit()

    # guessTheNumber()

    # rockPaperScissors()


if __name__ == "__main__":
    main()
