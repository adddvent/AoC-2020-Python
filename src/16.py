import numpy as np

with open('input16.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip() # 71 ; -


# ss = \
"""
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".strip() # - ; -


ss1, ss2, ss3 = ss.split('\n\n')

ranges_dict = {}
for s in ss1.splitlines():
    name, s2 = s.split(': ')
    sr1, sr2 = s2.split(' or ')
    rl = []
    for sr in [sr1, sr2]:
        rl.append(tuple(int(x) for x in sr.split('-')))
        assert len(rl[-1]) == 2
    ranges_dict[name] = rl

for i, s in enumerate(ss2.splitlines()):
    if i == 0:
        assert s == 'your ticket:'
    elif i == 1:
        own_ticket = [int(x) for x in s.split(',')]
    else: assert False

other_ticket_all = []
for i, s in enumerate(ss3.splitlines()):
    if i == 0:
        assert s == 'nearby tickets:'
    else:
        other_ticket_all.append([int(x) for x in s.split(',')])


# drop tickets that have values that do not match any of the ranges
other_ticket_all_new = []
invalid_nums = []
for other_ticket in other_ticket_all:
    for v in other_ticket:
        for (r1a, r1b), (r2a, r2b) in ranges_dict.values():
            if (r1a <= v <= r1b) or (r2a <= v <= r2b):
                break
        else:
            invalid_nums.append(v)
            break
    else:
        other_ticket_all_new.append(other_ticket)

res_a = sum(invalid_nums)

print('solution a:', res_a)

##

other_ticket_all = other_ticket_all_new

num_fields = len(ranges_dict)
ota = np.array(other_ticket_all)

cands_all = [set(range(num_fields)) for _ in range(num_fields)]

for ind_col, col in enumerate(ota.T):
    for i, ((r1a, r1b), (r2a, r2b)) in enumerate(ranges_dict.values()):
        if not np.all( ((r1a <= col) & (col <= r1b)) | ((r2a <= col) & (col <= r2b)) ):
            cands_all[ind_col].remove(i)


changed = True
while changed:
    changed = False
    for i, cands in enumerate(cands_all):
        if len(cands) == 1:
            v = list(cands)[0]
            for j, cands2 in enumerate(cands_all):
                if j == i:
                    continue
                if v in cands2:
                    cands2.remove(v)
                    changed = True

assert all(len(cands) == 1 for cands in cands_all)
cc_all = [list(cands)[0] for cands in cands_all]

names_all = list(ranges_dict)
names_sorted = [names_all[c] for c in cc_all]

res_b = 1
for v, name in zip(own_ticket, names_sorted):
    if name.startswith('departure'):
        res_b *= v


print('solution b:', res_b)
