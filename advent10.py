import numpy
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

with open('input.txt', "r") as file:
    input = file.read().splitlines()


def create_mapping(x):
    top = (x[0]-1, x[1])
    bottom = (x[0]+1, x[1])
    left = (x[0], x[1]-1)
    right = (x[0], x[1]+1)
    return {'F': [right, bottom], '-': [left, right], '7': [left, bottom], '|': [top, bottom], 'J': [top, left], 'L': [top, right]}


def find_connection(p, t, old_pos=False):
    ret = create_mapping(p)[t]
    if old_pos:
        ret.remove(old_pos)
        ret = ret[0]
    return ret


d = numpy.array([list(x) for x in input])
start = numpy.where(d=="S")

top = (start[0]-1, start[1])
bottom = (start[0]+1, start[1])
left = (start[0], start[1]-1)
right = (start[0], start[1]+1)

is_top, is_bottom, is_right, is_left = False, False, False, False

if d[top][0] in ['7', '|', 'F']:
    is_top = True

if d[bottom][0] in ['|', 'L', 'J']:
    is_bottom = True

if d[left][0] in ['L', '-', 'F']:
    is_left = True

if d[right][0] in ['-', 'J', '7']:
    is_right = True

if is_left and is_right: s = '-'
elif is_left and is_top: s = 'J'
elif is_left and is_bottom: s = '7'
elif is_right and is_top: s = 'L'
elif is_right and is_bottom: s = 'F'
elif is_top and is_bottom: s = '|'
else: print('ERROR!')

position = start
p_already = []
form = s
old_position = find_connection(position, form)[0]
i=0

while position not in p_already:
    p_already.append(position)
    ret = find_connection(position, form, old_position)
    old_position = position
    position = ret
    form = d[position][0]
    i+=1

print("Part 1: ", i/2)

polygon = Polygon(p_already)
counter = 0

for i in range(len(input[0])):
    for j in range(len(input)):
        point = Point(i, j)
        if polygon.contains(point):
            counter += 1

print("Part 2:", counter)