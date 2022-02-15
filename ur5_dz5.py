from functools import reduce

#5.1 Запись в файл набора чисел
# num1 = '787 705'
# with open('HT5#5.txt', 'a+') as file:
#     file.write(num1)

#5.2 Чтение из файла и подсчет суммы
file = open('HT5#5.txt', 'r')
r_file = file.read()

r_file = r_file.split()
val = reduce(lambda x,y: int(x)+int(y), r_file)
print("Сумма чисел в файле:", val)

file.close()