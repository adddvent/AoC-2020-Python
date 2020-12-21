with open('input10.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
16
10
15
5
1
11
7
19
6
12
4
""".strip() # 35 ; 8

# ss = \
"""
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip() # 220 ; 19208


vv0 = [int(s) for s in ss.splitlines()]
assert len(set(vv0)) == len(vv0)

max_diff = 3
vv0_sorted = sorted(vv0)
assert vv0_sorted[0] > 0

vv = [0] + vv0_sorted

vv_diff = [b - a for a, b in zip(vv[:-1], vv[1:])]

res_a = vv_diff.count(1) * (1 + vv_diff.count(3))

print('solution a:', res_a)

##

n = len(vv)

num_paths_list = [0] * n
num_paths_list[0] = 1
for i, v in enumerate(vv):
    num_paths_till_here = num_paths_list[i]
    for j in range(i+1, i+1+max_diff):
        if j < n and vv[j] - v <= max_diff:
            num_paths_list[j] += num_paths_till_here

res_b = num_paths_list[-1]

print('solution b:', res_b)
