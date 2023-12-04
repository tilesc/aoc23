import re
import pandas as pd

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

dic = {}
for e in input:
    data = e.split(':')[1].split(';')
    dic_1 = {}
    for n in range(len(data)):
        dic_2 = {}
        for col in data[n].split(','):
            dic_2[col.split()[1]] = int(col.split()[0])
        dic_1[n] = dic_2
    dic[e.split(':')[0]] = dic_1

sum = 0

for key, value in dic.items():
    red, green, blue = 0, 0, 0
    for key_1, value_1 in value.items():
        print(key, key_1, value_1)
        try:
            if value_1['red'] > red:
                red = value_1['red']
        except:
            pass
        try:
            if value_1['green'] > green:
                green = value_1['green']
        except:
            pass
        try:
            if value_1['blue'] > blue:
                blue = value_1['blue']
        except:
            pass
    print(red, green, blue)
    sum += red * green * blue