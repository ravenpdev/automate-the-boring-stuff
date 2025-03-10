def main():
    myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

    print(myCat["size"])
    print(myCat["color"])
    print(myCat["disposition"])

    for k, v in myCat.items():
        print(f"key: {k}, value: {v}")

    for k in myCat.keys():
        print(f"key: {k}")

    for v in myCat.values():
        print(f"value: {v}")

    if "fat" in myCat.keys():
        print(myCat["fat"])
    else:
        print("key doest not exist")

    # The get method takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exists.
    picnicItems = {"apples": 5, "cups": 2}
    print(f"I am bringing {picnicItems.get('cups', 0)} cups.")
    print(f"I am bringing {picnicItems.get('apples', 0)} apples.")
    print(f"I am bringing {picnicItems.get('pies', 0)} pies.")

    # The setdefault method
    # The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if they doest not exist,\
    # the setdefault() returns the key's value.
    dict1 = {"name": "raven", "age": 3}
    val = dict1.setdefault("hairColor", "black")
    print(dict1)
    print(val)
    val = dict1.setdefault("hairColor", "brown")
    print(val)


if __name__ == "__main__":
    main()
