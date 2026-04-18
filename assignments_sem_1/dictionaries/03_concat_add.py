"""Concat and add"""

dic1 = {1:10, 2:20, 4:6}
dic2 = {3:30, 4:40, 5:2}
dic3 = {5:50, 6:60}

result = {}

for d in (dic1, dic2, dic3):
    for k, v in d.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v

print(result)