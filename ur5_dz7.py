import json
print('#1\nНазвание, форма собственности, выручка, издержки')
with open("HT5#7.txt", 'r', encoding = 'utf-8') as f:
    A_cluster = []
    count = 0
    average_profit = 0
    df = dict()
    #count_df = 0
    for line in f:
        line = line.replace('.','')
        A = line.split()
        profit = int(A[2]) - int(A[3])
        print(f'Прибыль {A[1]} {A[0]} составила: {profit}')
        if profit > 0:
            count += 1
            average_profit += profit
    #2
        df[A[0]] = profit
    average_profit = average_profit/count
    dfa = {'average_profit':average_profit}
    print("Средняя прибыль кластера:", round(average_profit, 2), '\n')
    A_cluster.append(df)
    A_cluster.append(dfa)
    print('#2')
    print(A_cluster)

with open("HT5#7.json", 'a+') as f:
    f.write(str(A_cluster))

# print('\n#3\njson obj:')
# with open("HT5#7.json", 'r') as f:
#     for text in f:
#         print(text)