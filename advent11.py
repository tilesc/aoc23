import numpy as np
part1 = True

with open('input.txt', "r") as file:
    input = file.read().splitlines()

d = np.array([list(x) for x in input])

cols, rows = [], []
for col in range(len(d[0])):
    if '#' not in d[:, col]:
        cols.append(col)

for row in range(len(d)):
    if '#' not in d[row, :]:
        rows.append(row)

ii = np.where(d == '#')

empty_space_multi = 1 if part1 else 1000000 - 1

u = []
for i in range(len(ii[0])):
    r_add = np.sum(ii[0][i] > rows)
    c_add = np.sum(ii[1][i] > cols)
    u.append((ii[0][i]+empty_space_multi*r_add, ii[1][i]+empty_space_multi*c_add))

min_sum=0
for i in range(len(u)):
    for r in range(i+1,len(u)):
        min_sum+=abs(u[i][0]-u[r][0])+abs(u[i][1]-u[r][1])
