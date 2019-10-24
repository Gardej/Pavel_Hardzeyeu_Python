# 2. Найти и вывести наиболее часто встречаемый элемент в списке (любой, если их несколько).
# Список содержит целые числа от 1 до 100.
# Ввод: n - длина списка l - список длины n. Вывод: Наиболее часто встречаемый элемент

from collections import Counter
lin = []
n = int(input("Enter n: "))
for i in range(n):
    lin.append(int(input("Enter l(1...n): ")))
cnt = Counter(lin)
print(cnt.most_common()[0][0])


