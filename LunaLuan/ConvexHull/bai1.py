import random
import os
from collections import defaultdict


def line(a, b, p):
    ux = b['x'] - a['x']
    uy = b['y'] - a['y']
    nx, ny = -uy, ux
    return nx*(p['x']-a['x']) + ny*(p['y']-a['y'])


def encode(x):
    return str(x['x']) + '|' + str(x['y'])


datas = defaultdict(list)
curr = None
with open('test_case_1.in', 'r') as file:
    f = list(file)
    for idx, d in enumerate(f):
        temp = d.strip(' \n\r\t').split(' ')
        if len(temp) < 2:
            curr = temp[0]
        else:
            datas[curr].append({
                'x': int(temp[0]),
                'y': int(temp[1])
            })

for key, data in datas.items():
    lines = []
    for p1 in data:
        for p2 in data:
            lines.append({
                'p1': p1,
                'p2': p2
            })

    result = []
    for l in lines:
        left = 0
        right = 0
        for p in data:
            k = line(l['p1'], l['p2'], p)
            if k < 0:
                left = 1
            elif k > 0:
                right = 1
        if (left == 0 and right == 1) or (left == 1 and right == 0):
            # print(l)
            result.append(encode(l['p1']))
            result.append(encode(l['p2']))

    result = set(result)
    for r in result:
        temp = r.split('|')
        print(temp[0], temp[1])
