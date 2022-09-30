numbers = [1, 4, 2, 7, 4, 1]
print(numbers)
minn = min(numbers)
maxn = max(numbers)
p = []
for i in numbers:
    if i % 2 == 0:
        b = i * minn
        p.append(b)
    else:
        a = i * maxn
        p.append(a)
print(p)