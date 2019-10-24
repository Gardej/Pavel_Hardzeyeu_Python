# Word Order

from collections import OrderedDict

myd = OrderedDict()

for i in range(int(input())):
    key = input()
    if key not in myd.keys():
        myd.update({key: 1})
        continue
    myd[key] += 1

print(len(myd.keys()))
print(*myd.values())
