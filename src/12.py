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


cmd_param_all = [(s[0], int(s[1:])) for s in ss.splitlines()]


def apply_trans(cmd, num_steps, x, y):
    if cmd == 'N': y -= num_steps
    elif cmd == 'E': x += num_steps
    elif cmd == 'S': y += num_steps
    elif cmd == 'W': x -= num_steps
    return x, y


def apply_rot(cmd, degrees, dx, dy):
    num_rot90 = (degrees % 360) // 90
    if cmd == 'L':
        for _ in range(num_rot90):
            dy, dx = -dx, dy
    elif cmd == 'R':
        for _ in range(num_rot90):
            dy, dx = dx, -dy
    return dx, dy


r, c = 0, 0
dr, dc = 0, 1
for cmd, param in cmd_param_all:
    c, r = apply_trans(cmd, param, c, r)
    dc, dr = apply_rot(cmd, param, dc, dr)
    if cmd == 'F':
        r, c = r + param * dr, c + param * dc

res_a = abs(r) + abs(c)

print('solution a:', res_a)


r, c = 0, 0
dr, dc = 0, 1
dy, dx = r - 1, c + 10
for cmd, param in cmd_param_all:
    dx, dy = apply_trans(cmd, param, dx, dy)
    dx, dy = apply_rot(cmd, param, dx, dy)
    if cmd == 'F':
        r, c = r + param * dy, c + param * dx

res_b = abs(r) + abs(c)

print('solution b:', res_b)
