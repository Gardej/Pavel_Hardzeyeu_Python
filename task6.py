# Encription - task 6

alpha1 = 'abcdefghijklmnopqrstuvwxyz '
alpha2 = '0123456789ABCDEFGHIJKLMNOPQ'

insert = str(input())
content = ""
for i, j in enumerate(insert):
    content += alpha1[(alpha2.index(j) - i - 2) % 27]
print(content)
