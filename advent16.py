import numpy as np
import re
from collections import defaultdict

with open('input.txt') as f:
    input = f.read().splitlines()

input = [x.replace('/', 'f') for x in input]
input = [x.replace("\\", 'b') for x in input]

grid = np.array([list(x) for x in input])

DP = defaultdict(list)

d_dir = {'right': np.array([0,1]), 'left': np.array([0,-1]), 'up': np.array([-1,0]), 'down': np.array([1,0])}
n_dir = {str(v): k for k, v in d_dir.items()}


def get_activated_tiles(c, DP):
    hit = []
    marked = set()
    l=0
    marked.add(str(c[0][0]))

    for curr in c:

        new = []
        if str(curr[0])+'_'+curr[1] in DP.keys():
            o = DP[str(curr[0])+'_'+curr[1]]
            n = [x.split('_') for x in o]
            nrs = [re.findall(r'\d+', x[0]) for x in n]
            m = 0
            for x in nrs:
                new.append((np.array([int(x[0]), int(x[1])]), n[m][1]))
                m+=1

        else:
            n_loc = grid[tuple(curr[0])]

            if n_loc == '|' and (curr[1]=='right' or curr[1]=='left'):
                new.append((curr[0]+d_dir['up'], 'up'))
                new.append((curr[0]+d_dir['down'], 'down'))
            elif n_loc == '-' and (curr[1]=='up' or curr[1]=='down'):
                new.append((curr[0]+d_dir['left'], 'left'))
                new.append((curr[0]+d_dir['right'], 'right'))
            elif n_loc == 'b':
                switch = np.array([d_dir[curr[1]][1], d_dir[curr[1]][0]])
                new.append((curr[0]+switch, n_dir[str(switch)]))
            elif n_loc == 'f':
                switch = np.array([d_dir[curr[1]][1]*-1, d_dir[curr[1]][0]*-1])
                new.append((curr[0]+switch, n_dir[str(switch)]))
            else:
                new.append(((curr[0]+d_dir[curr[1]]), curr[1]))
        for n in new:
            if (0 <= n[0][0] < grid.shape[0]) and (0 <= n[0][1] < grid.shape[1]):
                if not str(n[0])+n[1] in hit:
                    c.append(n)
                    marked.add(str(n[0]))
                    if not str(n[0])+'_'+n[1] in DP[str(curr[0])+'_'+curr[1]]:
                        DP[str(curr[0])+'_'+curr[1]].append(str(n[0])+'_'+n[1])
            
        hit.append(str(curr[0]) + curr[1])

    return len(marked), DP.copy()


icount = 1
maxi = 0

for i in [0, grid.shape[0]-1]:
    for j in range(grid.shape[1]):
        print(icount)
        c = [(np.array([i,j]), 'down')]
        t, DP = get_activated_tiles(c, DP)
        if t >= maxi: maxi = t
        icount+=1

for j in [0, grid.shape[1]-1]:
    for i in range(1, grid.shape[0]-1):
        print(icount)
        c = [(np.array([i,j]), 'down')]
        t, DP = get_activated_tiles(c, DP)
        if t >= maxi: maxi = t
        icount+=1

print(maxi)