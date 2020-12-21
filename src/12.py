with open('input12.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
F10
N3
F7
R90
F11
""".strip() # 25 ; 286


r, c = 0, 0
dr, dc = 0, 1
for s in ss.splitlines():
    a, *aa = s
    mydir = a
    am = int(''.join(aa))
    if mydir == 'N': r -= am
    elif mydir == 'E': c += am
    elif mydir == 'S': r += am
    elif mydir == 'W': c -= am
    elif mydir == 'L':
        for _ in range((am % 360) // 90):
            dr, dc = -dc, dr
    elif mydir == 'R':
        for _ in range((am % 360) // 90):
            dr, dc = dc, -dr
    elif mydir == 'F':
        r, c = r + am * dr, c + am * dc

res_a = abs(r) + abs(c)

print('solution a:', res_a)



r, c = 0, 0
dr, dc = 0, 1

dy, dx = r - 1, c + 10

for s in ss.splitlines():
    a, *aa = s
    mydir = a
    am = int(''.join(aa))
    if mydir == 'N': dy -= am
    elif mydir == 'E': dx += am
    elif mydir == 'S': dy += am
    elif mydir == 'W': dx -= am
    elif mydir == 'L':
        for _ in range((am % 360) // 90):
            dy, dx = -dx, dy
    elif mydir == 'R':
        for _ in range((am % 360) // 90):
            dy, dx = dx, -dy
    elif mydir == 'F':
        r, c = r + am * dy, c + am * dx

res_b = abs(r) + abs(c)

print('solution b:', res_b)
