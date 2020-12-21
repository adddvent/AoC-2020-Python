import itertools

with open('input13.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
939
7,13,x,x,59,x,31,19
""".strip() # 295 ; 1068781


line1, line2 = ss.splitlines()
earliest_time = int(line1)
offset_period_all = [(i, int(x)) for i, x in enumerate(line2.split(',')) if x != 'x']

time_period_cands = []
for _, period in offset_period_all:
    a, rem = divmod(earliest_time, period)
    if rem > 0:
        a += 1
    bus_departure_time = a * period
    time_period_cands.append((bus_departure_time, period))

bus_departure_time, period = min(time_period_cands)
wait_time = bus_departure_time - earliest_time
res_a = period * wait_time

print('solution a:', res_a)



# offset_period_all = [(0, 7), (1, 13), (4, 59), (6, 31), (7, 19)] # 1068781
# offset_period_all = [(0, 7), (1, 13)] # 77
# offset_period_all = [(0, 7), (1, 13), (4, 59)] # 350
# offset_period_all = [(0, 7), (1, 13), (7, 19)] # 259
# offset_period_all = [(0, 7), (1, 13), (7, 19), (4, 59)] # 48671


"""
(x*p1 + off1 + off2) % p2 == 0
x = ((-off1 -off2) % p2) * p1inv
p1inv = pow(p1, -1, p2)
"""


def calc_cyclic_off_and_fact(off1, p1, off2, p2):
    p1inv = pow(p1, -1, p2)
    x = (-(off1 + off2) % p2) * p1inv
    # assert (x*p1 + off1 + off2) % p2 == 0
    p_new = p1 * p2
    off_new = (x * p1 + off1) % p_new
    return off_new, p_new


prev_off, fact = 0, 1
for off, p in offset_period_all:
    prev_off, fact = calc_cyclic_off_and_fact(prev_off, fact, off, p)

res_b = prev_off
print('solution b:', res_b)



if False:
    # very slow calculation - just for test data
    off_maxper, maxper = max(offset_period_all, key=lambda x: x[1])
    for k in itertools.count():
        t0 = k * maxper - off_maxper
        if t0 < 0:
            continue
        if all((t0 + off) % per == 0 for off, per in offset_period_all):
            print('result found:', t0)
            break
