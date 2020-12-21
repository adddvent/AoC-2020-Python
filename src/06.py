with open('input06.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip() # 11 ; 6


res_a = 0
res_b = 0
for ss_group in ss.split('\n\n'):
    union = set()
    common = None
    for s in ss_group.splitlines():
        set_s = set(s)
        union |= set_s
        if common is None:
            common = set_s
        else:
            common &= set_s
    res_a += len(union)
    res_b += len(common)


print('solution a:', res_a)
print('solution b:', res_b)
