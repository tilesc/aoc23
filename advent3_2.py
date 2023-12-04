import re

with open('input3.txt', 'r') as file:
    input = file.read().splitlines()

sum = 0
i = 0
d = {}
d_prior = {}

for l in input:
    d_prior[i] = [[m.span(), int(m.group())] for m in re.finditer(r'\d+', l)]
    i += 1

i = 0
for l in input:
    d[i] = [m.span() for m in re.finditer(r"[*]", l)]
    i += 1

for key, value in d.items():
    lower = key-1
    upper = key+1
    if lower < 0:
        lower = 0
    elif upper > len(input):
        upper = len(input)

    if value:
        for e in value:
            search_columns = [e[0]-1, e[1]+1]
            overlap_counter = 0
            digits = []
            for p in d_prior[lower]:
                if list(set(range(search_columns[0],search_columns[1])) & set(range(p[0][0], p[0][1]))):
                    overlap_counter += 1
                    digits.append(p[1])
            for p in d_prior[key]:
                if list(set(range(search_columns[0],search_columns[1])) & set(range(p[0][0], p[0][1]))):
                    overlap_counter += 1
                    digits.append(p[1])
            for p in d_prior[upper]:
                if list(set(range(search_columns[0],search_columns[1])) & set(range(p[0][0], p[0][1]))):
                    overlap_counter += 1
                    digits.append(p[1])
            print(overlap_counter, digits)
            if overlap_counter == 2:
                sum += digits[0] * digits[1]
