print('Enter text to write file "text.txt"\n')

with open("example_5.1.txt", 'w') as f:
    user_str = True
    while user_str:
        user_str = input()
        f.write(user_str + '\n')