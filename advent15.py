with open('input.txt') as f:
    input = f.read().split(',')

out = 0
for e in input:
    s=0
    for x in e:
        s = (s + ord(x))*17
        s = s % 256
    out+=s



ll = open('input.txt').read().strip().split(',')
p1 = 0
p2 = 0
def hash(l):
	v = 0
	for ch in l:
		v += ord(ch)
		v *= 17
		v %= 256
	return v
lenses = [[] for i in range(256)]
lenslengths = [{} for i in range(256)]
for i, l in enumerate(ll):
	p1 += hash(l)
	label = l.split("=")[0].split("-")[0]
	v = hash(label)
	if "-" in l:
		if label in lenses[v]:
			lenses[v].remove(label)
	if "=" in l:
		if label not in lenses[v]:
			lenses[v].append(label)
		lenslengths[v][label] = int(l.split("=")[1])
for box, lns in enumerate(lenses):
	for i, lens in enumerate(lns):
		p2 += (box + 1) * (i + 1) * lenslengths[box][lens]
print(p1, p2)