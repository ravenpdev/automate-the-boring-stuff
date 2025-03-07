import random


def hello() -> None:
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")


# def statements with parameters
def hello2(name: str) -> None:
    print(f"Hello, {name}")


# return values and return statements
def getAnswer(answer: int) -> str:
    if answer == 1:
        return "It is certain"
    elif answer == 2:
        return "It is decidedly so"
    elif answer == 3:
        return "Yes"
    elif answer == 4:
        return "Reply hazy try again"
    elif answer == 5:
        return "Ask again later"
    elif answer == 6:
        return "Concentrate and ask again"
    elif answer == 7:
        return "My reply is no"
    elif answer == 8:
        return "Outlook not so good"
    elif answer == 9:
        return "Very doubtful"
    else:
        return "Uknown"


# The Call Stack
# Call stack is how python remembers where to return the execution after each function call. The call stack isn't stored in a variable
# in your program; rather, Python handles it behind the scenes. When your program calls a function, Python create a frame object on the top of the call stack.
# Frame objects store the line number of the original function call so that Python can remember where to return. If another function call is made, Python puts
# another frame object on the call stack above the other one. When function call returns, Python removes a frame object from the top of the call stack and move
# the execution to the line number stored in it.


# Local and Global Scope
# Parameters and variables that are assigned in a called function are said to exist in the function's local scope.
# Variables that are assigned outside all functions are said to exist in the global scope.

# A Local scope is created whenever a fucntion is called. Any variables assigned in the function exist within the function's local scope.
# When the function returns, the local scope is destroyed, and these variables are forgotten. Local variables are also stored in frame object on the call stack.


# Scope matter for several reasons:
# - Code in the global scope, outside of all functions, cannot use any local variables.
# - However, code in a local scope can access global variables.
# - Code in a function's local scope cannot use variables in any other local scope.
# - You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable spam.


# Exception Handling
# - When to catch and re-raise an exception?
# - When to raise a new exception
# - When to chain exception
# - When to avoid using each of the above?


def divide(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError:
        # raise e  # Note: this is almost equivalent to bare `raise`
        print("Error: Invalid argument")


def main() -> None:
    # hello()
    # hello2("Raven")

    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)

    # There is a value called None, which represents the absence of a value. The None value is the only value of the NoneType data type.
    # Behind the scenes, Python add return None to the end of any function definition with no return statement. Also, if you use return statement
    # without a value, then None is returned.

    # Keyword arguments and the print() function
    # Keyword arguments are identified by the keyword put before them in the function call. Keyword arguments are often used for optional parameters.
    print("hello", "world", sep=",")

    result = divide(1, 0)
    print(result)


if __name__ == "__main__":
    main()
