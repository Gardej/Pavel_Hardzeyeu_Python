# Most common in list - task 2

from collections import Counter
lin = []
n = int(input("Enter n: "))
for i in range(n):
    lin.append(int(input("Enter l(1...n): ")))
cnt = Counter(lin)
print(cnt.most_common()[0][0])
