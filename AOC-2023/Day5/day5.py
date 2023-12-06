from functools import reduce

seeds, *mappings = open('input.txt').read().split('\n\n')
seeds = map(int, seeds.split()[1:])


def plant(start, mapping):
    for m in mapping.split('\n')[1:]:
        dst, src, len = map(int, m.split())
        delta = start - src
        if delta in range(len):
            return dst + delta
    else:
        return start


print(f"Part 1: {min(reduce(plant, mappings, int(s)) for s in seeds)}")
