'''
Задание 2: Скорость ракеты
Ракета запускается с точки на экваторе и развивает скорость v км/с. Каков результат
запуска?
Указание: если v ≤ 7.8 км/с, то ракета упадет на Землю (вывести 0), если 7.8 <v <11.2, то
ракета станет спутником Земли (вывести 1), если 11.2 ≤ v ≤ 16.4 , то ракета станет
спутником Солнца (вывести 2), если v > 16.4, то ракета покинет Солнечную Систему
(вывести 3).
Если будет введено значение, меньшее или равное 0, то вывести "error".
'''

v = int(input())
if (v > 0) and (v <= 7.8):
    print(0)
elif (v > 7.8) and (v < 11.2):
    print(1)
elif (v >= 11.2) and (v <= 16.4):
    print(2)
elif (v > 7.8):
    print(3)
else:
    print('error')