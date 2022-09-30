s = int(input())
b = type(s)
if (s >= 0) and (b == int) and 4<=len(str(s))<=6:
    print('yes')
else:
    print('no')