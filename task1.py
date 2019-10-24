# List Comprehensions

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))
ar = []
p = 0
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if (i + j + k) != n:
                ar.append([])
                ar[p] = [i, j, k]
                p += 1
print(ar)

