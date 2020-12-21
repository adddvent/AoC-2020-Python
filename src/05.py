with open('input05.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
FBFBBFFRLR
""".strip() # 357 ; -


seat_id_others = []

for s in ss.splitlines():
    seat_id = int(s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
    seat_id_others.append(seat_id)

res_a = max(seat_id_others)

print('solution a:', res_a)


seat_id_all = set(range(min(seat_id_others), max(seat_id_others)+1))
seat_id_empty = seat_id_all - set(seat_id_others)
res_b, = list(seat_id_empty)

print('solution b:', res_b)
