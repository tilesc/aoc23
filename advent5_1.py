import re

with open('seed-to-soil.txt', 'r') as file:
    seedsoil = file.read().splitlines()

with open('soil-to-fertilizer.txt', 'r') as file:
    soilfert = file.read().splitlines()

with open('fertilizer-to-water.txt', 'r') as file:
    fertwater = file.read().splitlines()

with open('water-to-light.txt', 'r') as file:
    waterlight = file.read().splitlines()

with open('light-to-temperature.txt', 'r') as file:
    lighttemp = file.read().splitlines()

with open('temperature-to-humidity.txt', 'r') as file:
    temphumid = file.read().splitlines()

with open('humidity-to-location.txt', 'r') as file:
    humidloc = file.read().splitlines()

seeds = [79, 14, 55, 13]

dict = {}

names = ['seedsoil', 'soilfert', 'fertwater', 'waterlight', 'lighttemp', 'temphumid', 'humidloc']
i=0
for cat in [seedsoil, soilfert, fertwater, waterlight, lighttemp, temphumid, humidloc]:
    dict[names[i]] = []
    for l in cat:
        x = [int(x) for x in l.split()]
        print(x[0]+x[2], x[1]+x[2], x[2])
        dict[names[i]].append({'dest_range': range(x[0], x[0]+x[2]), 'source_range': range(x[1], x[1]+x[2])})
    i+=1

i = 0

res_dict = {}
res = []
for s in seeds:
    is_range = False
    for x in dict['seedsoil']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s


i+=1

for s in res_dict.values:
    is_range = False
    for x in dict['soilfert']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s

i+=1
for s in res_dict.values:
    is_range = False
    for x in dict['fertwater']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s

i+=1
for s in res_dict.values:
    is_range = False
    for x in dict['waterlight']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s

i+=1
for s in res_dict.values:
    is_range = False
    for x in dict['lighttemp']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s

i+=1
for s in res_dict.values:
    is_range = False
    for x in dict['temphumid']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s
i+=1
for s in res_dict.values:
    is_range = False
    for x in dict['humidloc']:
        if s in x['source_range']:
            res_dict[names[i] + str(s)] = x['dest_range'][0] + (s - x['source_range'][0])
            is_range = True
    if not is_range:
        res_dict[names[i] + str(s)] = s