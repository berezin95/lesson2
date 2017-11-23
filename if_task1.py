age = int(input("Введи возраст: "))

#print(age)

if age <= 0:
    print('Веди положительное число')
elif age < 6:
    print('Ходи в детский сад')
elif age < 17:
    print('Ходи в школу')
elif age < 22:
    print('Ходи в универ')
elif age < 60:
    print('Работай')
elif age < 100:
    print('Получай пенсию')
else:
    print('Вряд ли ты жив :)')
