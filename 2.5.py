col = int(input())

k1 = []
k2 = []
for i in range(col):
    dann = input()
    dann = dann.split()
    if 20<=int(dann[1])<=40:
        k2.append(dann[0])
    else:
        k1.append(dann[0])
list.sort(k1)
list.sort(k2)
print('Команда 1: ', k1)
print('Команда 2: ', k2)



