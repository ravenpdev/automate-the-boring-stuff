import pprint


def main():
    message = "It was a bright cold day in April, and the clocks wre striking thirteen."
    count: dict[str, int] = {}

    for character in message:
        _ = count.setdefault(character, 0)
        count[character] = count[character] + 1

    pprint.pprint(count)
    print(pprint.pformat(count, indent=2))


if __name__ == "__main__":
    main()
