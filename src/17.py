import itertools

with open('input17.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
.#.
..#
###
""".strip() # 112 ; 848


def calc_conway_cubes(occupied_fields, num_cycles=6, use_w_dimension=False):
    if use_w_dimension:
        dw_list = [-1, 0, 1]
    else:
        dw_list = [0]

    for i in range(num_cycles):
        occupied_fields_new = set()

        fields_to_check = set()
        for (x, y, z, w) in occupied_fields:
            for dx, dy, dz, dw in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], dw_list):
                fields_to_check.add((x+dx, y+dy, z+dz, w+dw))

        for (x, y, z, w) in fields_to_check:
            num_active_neighbors = 0
            v = (x, y, z, w) in occupied_fields
            for dx, dy, dz, dw in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], dw_list):
                if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                    continue
                x2, y2, z2, w2 = x+dx, y+dy, z+dz, w+dw
                if (x2, y2, z2, w2) in occupied_fields:
                    num_active_neighbors += 1

            if v and num_active_neighbors in [2, 3]:
                occupied_fields_new.add((x, y, z, w))
            elif not v and num_active_neighbors == 3:
                occupied_fields_new.add((x, y, z, w))

        occupied_fields = occupied_fields_new

    return occupied_fields



occupied_fields = set()
for y, s in enumerate(ss.splitlines()):
    for x, c in enumerate(s):
        if c == '#':
            occupied_fields.add((x, y, 0, 0))


occupied_fields_new = calc_conway_cubes(occupied_fields, num_cycles=6, use_w_dimension=False)
res_a = len(occupied_fields_new)

print('solution a:', res_a)


occupied_fields_new = calc_conway_cubes(occupied_fields, num_cycles=6, use_w_dimension=True)
res_b = len(occupied_fields_new)

print('solution b:', res_b)
