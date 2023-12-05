def convert_to_next(ranges, conv_rule):
    conv_nrs = []
    for start, length in ranges:
        is_found = False
        end = start + length
        for t in conv_rule:
            source_start = t[0]
            source_end = source_start + t[2]
            destin_start = t[1]
            # check if overlap and cut off non-overlap to check again
            if start < source_end and end > source_start:
                is_found = True
                conv_start = destin_start + (max(start, source_start) - source_start)
                conv_nrs.append((conv_start, min(end, source_end) - max(start, source_start)))
                # very slow to append to original list again
                if start < source_start: ranges.append((start, source_start - start))
                if end > source_end: ranges.append((source_end, end - source_end))
        # if no overlap at all with any source range of the conversion stage
        if not is_found: conv_nrs.append((start, length))
    return conv_nrs


with open('input.txt', "r") as file:
    input = file.read()
conversions = input.split('\n\n')

names = ['seedsoil', 'soilfert', 'fertwater', 'waterlight', 'lighttemp', 'temphumid', 'humidloc']

i = 0
data = {}

for s in conversions:
    if i == len(names): break
    # pull out first row with seed ranges -> different method
    if s[:5] == 'seeds':
        m = input.splitlines()[0].split(': ')[1].split()
        input_ranges = [(int(m[i]), int(m[i + 1])) for i in range(0, len(m), 2)]
        continue
    else: 
        t = [m.split() for m in s.split(':\n')[1].splitlines()]
        data[names[i]] = [(int(m[1]), int(m[0]), int(m[2])) for m in t]
    i += 1

for n in names:
    input_ranges = convert_to_next(input_ranges, data[n])

print('Result Part 2:', min([t[0] for t in input_ranges]))
