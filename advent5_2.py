with open('input.txt', "r") as file:
    input = file.read()


def to_tuple(s):
    _s = s.split(':\n')[1].splitlines()
    t = [m.split() for m in _s]
    u = [(int(m[1]), int(m[0]), int(m[2])) for m in t]
    return u


def convert_to_next(ranges, conv_rule):
    output = []
    for start, length in ranges:
        is_found = False
        end = start + length

        for t in conv_rule:
            source_start = t[0]
            source_end = source_start + t[2]
            destin_start = t[1]

            if start < source_end and end > source_start:
                is_found = True

                out_start = destin_start + (max(start, source_start) - source_start)
                output.append((out_start, min(end, source_end) - max(start, source_start)))

                if start < source_start:
                    length = (source_start - start)
                    ranges.append((start, length))

                if end > source_end:
                    start = source_end
                    length = end - source_end
                    ranges.append((start, length))

        if not is_found:
            output.append((start, length))

    return output


names = ['seedsoil', 'soilfert', 'fertwater', 'waterlight', 'lighttemp', 'temphumid', 'humidloc']

parts = input.split('\n\n')
i = 0

data = {}
for s in parts:
    if i == len(names):
        break
    if s[:5] == 'seeds':
        m = input.splitlines()[0].split(': ')[1].split()
        seed_rng = [(int(m[i]), int(m[i + 1])) for i in range(0, len(m), 2)]
        continue
    else:
        data[names[i]] = to_tuple(s)
    
    i += 1

input_ranges = seed_rng

outs = {}
for n in names:
    input_ranges = convert_to_next(input_ranges, data[n])
    outs[n] = input_ranges.copy()

print('Result Part 2:', min([t[0] for t in input_ranges]))
