day = int(input("Введите число дня недели от 1 до 7: "))

if day >= 1 and day <= 5:
    print("Это рабочий день!")
elif day >= 6 and day <= 7:
    print("Это выходной!")
else:
    print("Вы вели некоректно день недели")