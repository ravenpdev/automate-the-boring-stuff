import random
import time


def main():
    numberOfStreaks = 0

    for _ in range(10_000):
        # flips: list[str] = []
        # for _ in range(100):
        #     flip = random.randint(0, 1)
        #     if flip == 0:
        #         flips.append("H")
        #     else:
        #         flips.append("T")
        flips = [random.choice(["H", "T"]) for _ in range(100)]

        # print(flips)
        # time.sleep(10)

        streaks = 1
        for i in range(len(flips)):
            if flips[i] == flips[i - 1]:
                streaks += 1
                if streaks == 6:
                    numberOfStreaks += 1
                    break
            else:
                streaks = 1

        # headCount = 0
        # for i in range(len(flips)):
        #     if flips[i] == "H" and flips[i - 1] == "H":
        #         headCount += 1

        #         if headCount == 6:
        #             numberOfStreaks += 1
        #             break
        #     else:
        #         headCount = 0

        # tailCount = 0
        # for i in range(len(flips)):
        #     if flips[i] == "T" and flips[i - 1] == "T":
        #         tailCount += 1

        #         if tailCount == 6:
        #             numberOfStreaks += 1
        #             break
        #     else:
        #         tailCount = 0

    print(f"Chance of streaks: {numberOfStreaks / 10_000 * 100}%")


if __name__ == "__main__":
    main()
