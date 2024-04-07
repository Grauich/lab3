def slovavmeste():
    N = int(input("Количество слов: "))
    slovokstroka = ""

    for i in range(N):
        slovo = input("Введите слово: ")
        slovokstroka += slovo + " "

    print("Ваши слова:", slovokstroka)


slovavmeste()
