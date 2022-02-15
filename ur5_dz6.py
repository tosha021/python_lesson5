data = []
num = []
with open("HT5#6.txt", 'r', encoding = 'utf-8') as f:
    for line in f:
        str_c = ''
        num_c = ''
        flag = 0
        flag2 = 0
        for x in line:
            if x.isupper() or flag == 1:
                flag = 1
                if x == ':':
                    flag = 0
                else:
                    str_c += x
            elif x.isdigit() or flag2 == 1:
                flag2 = 1
                if x.isdigit() != True:
                    num_c += ' '
                    flag2 = 0
                else:
                    num_c += x
            else:
                pass
        data.append(str_c)
        count = 0
        A = num_c.split()
        num_c = 0
        for n in A:
            num_c += int(n)
        num.append(num_c)
# print(data)
# print(num)

d = {data[i]:num[i] for i in range(len(data))}
print(d)