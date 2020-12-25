ss = '158937462'

# ss = '389125467' # 67384529 ; 149245887792


def calc_game(initial_cups, num_moves, num_cups=None):
    if num_cups is None:
        num_cups = len(initial_cups)

    if len(initial_cups) < num_cups:
        initial_cups = initial_cups + list(range(len(initial_cups)+1, num_cups+1))

    nn_dict = {} # right neighbor dict
    prev_cup = initial_cups[-1]
    for cup in initial_cups:
        nn_dict[prev_cup] = cup
        prev_cup = cup

    cur = initial_cups[0]

    for ind_move in range(num_moves):
        removed_cups = []
        cur1 = cur
        for ind_remove in range(3):
            cur = nn_dict[cur]
            removed_cups.append(cur)
        cur = nn_dict[cur]
        nn_dict[cur1] = cur

        dest_cup = cur1 - 1
        if dest_cup == 0:
            dest_cup = num_cups
        while dest_cup in removed_cups:
            dest_cup -= 1
            if dest_cup == 0:
                dest_cup = num_cups

        cur = dest_cup
        cur2 = nn_dict[dest_cup]
        for rc in removed_cups:
            nn_dict[cur] = rc
            cur = rc
        nn_dict[cur] = cur2

        cur = nn_dict[cur1]

    return nn_dict



initial_cups = [int(c) for c in ss]


nn_dict = calc_game(initial_cups, 100)

cur = 1
rr = []
for _ in range(len(nn_dict) - 1):
    cur = nn_dict[cur]
    rr.append(str(cur))

res_a = ''.join(rr)
print('solution a:', res_a)



nn_dict = calc_game(initial_cups, 10_000_000, 1_000_000)

res_b = 1
cur = 1
for _ in range(2):
    cur = nn_dict[cur]
    res_b *= cur
print('solution b:', res_b)
