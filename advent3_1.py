import re

with open('input3.txt', 'r') as file:
    input = file.read().splitlines()

special_characters = "!@#$%^&*()-+?_=,<>/"

sum = 0
i = 0
d = {}

for l in input:
    d[i] = [[m.span(), int(m.group())] for m in re.finditer(r'\d+', l)]
    i += 1

for key, value in d.items():
    search_rows = [key-1, key+2]

    if search_rows[0] < 0:
        search_rows[0] = 0
    
    r_to_check = input[search_rows[0]:search_rows[1]]

    for e in value:
        search_columns = [e[0][0]-1, e[0][1]+1]
        if search_columns[0] < 0:
            search_columns[0] = 0
        is_special = False
        for _l in r_to_check:
            if not is_special:
                is_special = any(c in special_characters for c in _l[search_columns[0]:search_columns[1]])
        if is_special:
            sum += e[1]
        else:
            print(e[1], search_columns, search_rows)
