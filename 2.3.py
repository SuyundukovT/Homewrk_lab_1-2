n = int(input('количество эл списка: '))
b = []
d = []
n_min = int(input('min: '))
n_max = int(input('max: '))
import random
for i in range(n):
    c = random.uniform(-10,10)
    b.append(c)
    if n_min <= c <= n_max:
        d.append(c)
print('начальный: ', b)
print('конечный: ', d)
print('количество: ', len(d))