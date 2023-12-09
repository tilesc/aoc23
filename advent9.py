import operator

def mapper(x):
    c = []
    c.append(x)
    while not all(v == 0 for v in x):
        x = list(map(operator.sub, x[1:], x[:-1]))
        c.append(x.copy())
    return c


with open('input.txt', "r") as file:
    input = file.read().splitlines()
input = [list(map(int, x.split())) for x in input]

res1 = []
res2 = []

for x in input:
    m = mapper(x)
    l = 0
    n = 0
    for e in m[::-1]:
        l += e[-1]
        n = e[0] - n
    res1.append(l)
    res2.append(n)

sum(res1)
sum(res2)
