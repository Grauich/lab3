def slovavmeste():
    slovokstroka = ""

    while True:
        slovo = input("Вводите слова, а как надоест - пропишите 'stop': ")
        if slovo.lower() == "stop": 
            break
        slovokstroka += slovo + " "  

    print("Результат соединения слов:", slovokstroka)

slovavmeste()

