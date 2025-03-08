import random


def main() -> None:
    names = ["raven", "kristine", "iya", "elia"]

    for name in names:
        print(name)

    emptyList: list[int] = []
    print(len(emptyList))
    if len(emptyList) == 0:
        print("emptyList is empty")

    # if len(emptyList) == 0:
    #     print("empty list")

    # for immutable data types, slicing behaves like a deep copy
    fruits = ["apple", "banana", "orange", "watermelon"]
    favFruits = fruits[:2]

    print(favFruits)
    favFruits[0] = "grapes"
    print(fruits, favFruits)

    # for mutable objects (list, dictionaries, set), slicing create a shallow copy
    programmingLanguages = [["go", "zig", "ust"], ["python", "php", "ruby"]]
    # programming = programmingLanguages.copy()
    programming = programmingLanguages[:]
    print(programming)
    # this will change the value for both programmingLanguages and programming
    programming[0][0] = "odin"
    print(programmingLanguages, programming)

    # List concatenation and list replication
    listA = [1, 2, 3]
    listB = [4, 5, 6]
    listC = listA + listB
    print(listC)
    listD = listC * 2
    print(listD)

    # Removing the value from lists with del statement
    nums = [1, 2, 3, 4]
    print(nums)
    del nums[0]
    print(nums)

    for i in range(len(nums)):
        print(f"Index {i} in nums is {nums[i]}")

    # The in and not operators
    greeting = ["Hi", "Hello", "Howdy", "Bonjour"]
    print("Hi" in greeting)
    print("Bonjour" in greeting)
    print("test" in greeting)

    # Iterable unpacking
    cat = ["fat", "gray", "loud"]
    size, color, disposition = cat
    print(f"my cat is {size} color {color} and it is {disposition}")

    # Using the enumerate with lists
    # The enumerate function is useful if you need both index and the item
    supplies = ["pens", "staplers", "flamethrowers", "binders"]
    for i, val in enumerate(supplies):
        print(f"index: {i} value: {val}")

    rand1 = random.choice(supplies)
    print(f"using random.choice, value: {rand1}")
    print(f"before shuffle {supplies}")
    random.shuffle(supplies)
    print(f"after shuffle {supplies}")

    # Augmented assignment operator
    # n += 1 == n = n + 1
    # n -= 1 == n = n - 1
    # n *= 1 == n = n * 1
    # n /= 1 == n = n / 1
    # n %= 1 == n = n % 1

    # Removing value from list with the remove method()
    # Attempting to delete a value that does not exist will result in a ValueError error.
    animals = ["cat", "bat", "rat", "elephant"]
    animals.remove("bat")
    print(animals)

    # Sorting the values in the list with the sort() method
    nums = [2, 5, 3.14, 1, -7]
    nums.sort()
    print(nums)
    animals.sort()
    animals.sort(reverse=True)
    print(animals)

    # You cannot sort lists that have both number values and string values in them.
    mix = [1, 2, 3, 4, "Alice", "Bob"]
    # mix.sort()  # TypeError
    print(mix)

    # sort() uses "ASCIIbetial order". This means uppercase letter comes before lowercase letter.
    # this causes the sort() method to treat all items in the list as if they were lowercase without actually chaning the values in the list.
    mix = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
    mix.sort()
    print(mix)
    mix.sort(key=str.lower)
    print(mix)

    # revers() the order
    mix.reverse()
    print(mix)

    # Sequence Data Types
    # The Python sequence data types includes lists, strings, range object returned by range(), and tuples
    name = "raven"
    for c in name:
        print(f"*****{c}*****")

    # Mutable and Immutable Data Types
    # A list value is a mutable data type: it can have values added, removed, or changed.
    # A string is immutable; it cannot be changed
    name = "Zophie a cat"
    # name[7] = 'the'
    newName = name[:7] + "the" + name[8:]
    print(name)
    print(newName)

    # The Tuple Data Type
    # Tuples are immutable
    person = ("raven", 32, "male")
    print(person)
    print(type(("hello",)))  # to indicate that it is a tuple with single value
    print(type(("hello")))  # this will print str instead of tuple

    # Converting types with the list() and tuple() functions
    tup = tuple(["cat", "dog", 5])
    print(tup)

    lst = list(("cat", "dog", 5))
    print(lst)

    print(id("howdy!"))
    greet = "Hello"
    print(id(greet))
    greet += " world!"
    print(id(greet))


if __name__ == "__main__":
    main()
