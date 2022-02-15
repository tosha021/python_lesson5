file = open('HT5#4.txt', 'r', encoding='utf-8')
A = ['One', 'Two', 'Three', 'Four']
B = ['Один', 'Два', 'Три', 'Четыре']

for line in file:
    words = line.split()
    for i in range(len(words)):
        for j in range(len(A)):
            if words[i] == A[j]:
                words[i] = B[j]

    new = [' '.join(words[0:])]
    new = new[0] + '\n'
    with open('HT5#4_2.txt', 'a+') as file2:
        file2.write(new)