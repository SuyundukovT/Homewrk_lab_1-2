# Задание 5: Улыбающийся текст
# Вводится текстовая переменная s, в которой нужно заменить все знаки препинания на
# смайлики (':)'). Знаками препинания считайте символы: точка, запятая, двоеточие, тире
# (дефис), восклицательный и вопросительный знаки. Результат выведите на экран.
# Пример: 'Привет, Андрей!' → 'Привет:) Андрей:)'
# При выполнении задания рекомендуется использовать строковый метод replace()

s = 'gig, mbmn.ghggfhg!gyjgjgu?uhiuh:bk'
s = s.replace(':',':)')
s = s.replace('.',':)')
s = s.replace('?',':)')
s = s.replace('-',':)')
s = s.replace('!',':)')
s = s.replace(',',':)')
print(s)