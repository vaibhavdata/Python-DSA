from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    item = input().split()
    item_price = int(item[-1])
    item_name = " ".join(item[:-1])
    if (d.get(item_name)):
        d[item_name] += item_price
    else:
        d[item_name] = item_price
for i in d.keys():
    print(i,d[i])