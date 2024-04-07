def redkoeslovo(slovo):
    return 'ф' in slovo.lower()


def main():
    while True:
        user = input("Вводите слова, а как надоест - пропишите 'stop': ")
        if user.lower() == "stop":
            print("Программа завершена.")
            break

        if redkoeslovo(user):
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")

main()