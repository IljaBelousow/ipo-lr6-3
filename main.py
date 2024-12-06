#Запрашивает у пользователя количество строк. (должно быть проверка)
spisok = []
j = 0
a = input("введите колво слов: ")
if a.isdigit() and int(a) > 0:#если все цифры и int > 0
    kolvo = int(a)
        
    for i in range(kolvo):#i по длине kolvo
        b = input("введите слово ")
        spisok.append(b)
    print(spisok)
    word = set(spisok)#множество spisok
    for i in word:
        spisok_count = spisok.count(i)#проверяет сколько раз i вошло в функцию
        print(i, "повторилась ", spisok_count)

    
else:
    print("!!!!!!!!!!!! Введите нормально!!!!!!!!!!!!")
    
