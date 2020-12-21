with open('input02.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip() # 2 ; 1


res_a = 0
res_b = 0
for s in ss.splitlines():
    s1, pwd = s.split(': ')
    s_range, c = s1.split()
    n1, n2 = (int(x) for x in s_range.split('-'))
    cnt_c = pwd.count(c)
    if n1 <= cnt_c <= n2:
        res_a += 1
    if (pwd[n1 - 1] == c) ^ (pwd[n2 - 1] == c):
        res_b += 1


print('solution a:', res_a)
print('solution b:', res_b)
