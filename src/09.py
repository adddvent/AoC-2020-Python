import itertools
from collections import deque

with open('input09.txt', 'rt') as fd:
    ss = fd.read().strip()

preamble = 25


# preamble = 5; ss = \
"""
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip() # 127 ; 62


vv = [int(s) for s in ss.splitlines()]


qq = deque(vv[:preamble], preamble)

for v in vv[preamble:]:
    found = False
    # check if v == a + b is in qq
    for a in qq:
        b = v - a
        if b > 0 and b in qq:
            if b == a and qq.count(a) <= 1:
                continue
            found = True
            break
    if not found:
        break
    qq.append(v)
else:
    assert False

res_a = v
print('solution a:', res_a)


for window_size in itertools.count(2):
    qq = deque(vv[:window_size], window_size)
    wsum = sum(qq)
    for v in vv[window_size:]:
        if wsum == res_a:
            break
        wsum -= qq.popleft()
        qq.append(v)
        wsum += v
    else:
        continue
    break

res_b = max(qq) + min(qq)

print('solution b:', res_b)
