from collections import defaultdict

with open('input.txt') as f:
    input = f.read().split(',')


def run_hash(label):
    s = 0
    for x in label:
        s = (s + ord(x))*17
        s = s % 256
    return s


d = defaultdict(list)

for s in input:
    pos = s.find('-')
    if pos == -1:
        pos = s.find('=')
        box = run_hash(s[:pos])
        in_box = [i for i in d[box] if s[:pos] in i]
        if in_box:
            d[box] = list(map(lambda x: x.replace(in_box[0], s[:pos] + s[pos+1:]), d[box]))
        else:
            d[box].append(s[:pos] + s[pos+1:])
    else:
        box = run_hash(s[:pos])
        in_box = [i for i in d[box] if s[:pos] in i]
        for l in in_box:
            d[box].remove(l)

out = 0
for b, ls in d.items():
    i=1
    for l in ls:
        out+=(1+b)*i*int(l[-1])
        i+=1