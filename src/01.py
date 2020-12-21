import itertools

with open('input01.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
1721
979
366
299
675
1456
""".strip() # 514579 ; 241861950


vv = [int(s) for s in ss.splitlines()]

for a, b in itertools.combinations(vv, 2):
    if a + b == 2020:
        res_a = a * b
        break
else:
    assert False

print('solution a:', res_a)


for a, b, c in itertools.combinations(vv, 3):
    if a + b + c == 2020:
        res_b = a * b * c
        break
else:
    assert False

print('solution b:', res_b)
