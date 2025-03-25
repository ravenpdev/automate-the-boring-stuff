def main() -> None:
    birthdays = {
        "kristine": "Jul 07",
        "raven": "nov 29",
        "iya": "sept 01",
        "elia": "feb 20",
    }

    while True:
        name = input("Enter your name: ")

        if name == "":
            break

        if name in birthdays.keys():
            print(f"{name} birthday is: {birthdays[name]}")
        else:
            print(f"I don't have the birthday information for {name}")
            bday = input("What is their birthday? ")
            birthdays[name] = bday
            print("Database updated!")
        # try:
        #     print(birthdays[name])
        # except KeyError:
        #     print("Key not found!")
        #     continue


if __name__ == "__main__":
    main()
