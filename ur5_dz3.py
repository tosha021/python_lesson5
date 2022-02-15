from functools import reduce
file = open('HT5#3.txt', 'r', encoding='utf-8')
salary = []
low_salary = []
cost = 20000.00
for line in file:
    symbols = len(line)
    words = line.split()
    for ty in words:
        try:
            ty = float(ty)
        except ValueError:
            pass
        if type(ty) is float:
            salary.append(ty)
            if ty < cost:
                low_salary.append(words)
file.close()
mean_salary = (reduce(lambda x,y: x + y, salary) / len(salary))
print('Сотрудники с з/п < 20000.00: ')
count = 0
for person in low_salary:
    count += 1
    print(f'{count}. {person[0]}')

print('\nСредняя величина дохода сотрудников: ', round(mean_salary, 2))