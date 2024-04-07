import random


def randomer():
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    return n1, n2


def main():
    win = 0
    loos = 0

    while loos < 3:
        n1, n2 = randomer()
        slojenie = f"{n1} + {n2} = "
        answer = int(input(slojenie))

        if answer == n1 + n2:
            print("Правильно!")
            win += 1
        else:
            print("Ответ неверный")
            loos += 1

    print(f"Игра окончена. Правильных ответов: {win}")


main()
