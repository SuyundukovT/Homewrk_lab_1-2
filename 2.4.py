a = int(input())
c = []
if a >= 4:
    for i in range(a):
        b = int(input())
        c.append(b)
    print(c)
    mini = min(c)
    maxi = max(c)
    c.remove(mini)
    c.remove(maxi)
    print(c)
else:
    print('error')