with open("example_5.1.txt") as f:
    content = f.readlines()
print(f'Количество строк в файле - {len(content)}')
for index, el in enumerate(content):
    print(f'Строка {index+1} - слов {len(el.split(" "))}')