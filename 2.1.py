words = ['biba', 'bobabo', 'mira', 'gig']
my_list = list(map(len, words))
print(words)
result = min(my_list) + max(my_list)
print(result)