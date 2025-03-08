import random


def main() -> None:
    messages = [
        "It is certain",
        "It is decidedly so",
        "Yes definitely",
        "Reply hazy try again",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook not so good",
        "Very doubtful",
    ]

    print(random.choice(messages))


if __name__ == "__main__":
    main()
