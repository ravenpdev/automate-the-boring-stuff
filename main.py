def main() -> None:
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("Oopsie! You can't divide by zero")

    # List Comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = [n for n in numbers if n % 2 == 0]
    print(even)
    odd = [n for n in numbers if n % 2 == 1]
    print(odd)


if __name__ == "__main__":
    main()
