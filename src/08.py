with open('input08.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip() # 5 ; 8


cmd_all = []
for s in ss.splitlines():
    cmd, s2 = s.split()
    param = int(s2)
    cmd_all.append([cmd, param])


def run_commands(cmd_all):
    visited = set()
    i = 0
    acc = 0
    n = len(cmd_all)
    while i < n:
        cmd, param = cmd_all[i]
        if i in visited:
            return 'loop', acc
        visited.add(i)
        i_next = i + 1
        if cmd == 'nop':
            pass
        elif cmd == 'acc':
            acc += param
        elif cmd == 'jmp':
            i_next = i + param
        else: assert False
        i = i_next
    else:
        return 'done', acc


status, acc = run_commands(cmd_all)
assert status == 'loop'

res_a = acc
print('solution a:', res_a)


inverted_nop_jmp = {'nop': 'jmp', 'jmp': 'nop'}

for cmd in cmd_all:
    if cmd[0] in inverted_nop_jmp:
        cmd[0] = inverted_nop_jmp[cmd[0]]
        status, acc = run_commands(cmd_all)
        if status == 'done':
            break
        cmd[0] = inverted_nop_jmp[cmd[0]] # change back to original value
else:
    assert False

res_b = acc
print('solution b:', res_b)
