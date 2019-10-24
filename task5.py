# Клавиатура. Задача 66.

string = 'qwertyuiopasdfghjklzxcvbnmq'
for i in string:
    i = input()
    print(string[string.index(i) + 1])
    break
