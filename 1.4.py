'''
Задание 4. Определение домена
Вводится адрес электронной почты в переменную email. Напишите универсальный код, с
помощью которого можно извлечь из этого адреса адрес домена.
Пример: 'vasya@mail.ru' → 'mail.ru'
При выполнении задания рекомендуется использовать строковый метод find()
'''

p = input()
b = p.find('@') + 1
print(p[b:])
