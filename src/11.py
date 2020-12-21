import itertools

with open('input11.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip() # 37 ; 26


def calc_seating(ss, mode='a'):
    is_seat = [[c != '.' for c in row] for row in ss.splitlines()]
    num_rows, num_cols = len(is_seat), len(is_seat[0])

    is_occu = [[False]*num_cols for _ in range(num_rows)]

    if mode == 'a':
        n2 = 2
        max_comfortable_neighbors = 4
    elif mode == 'b':
        n2 = max(num_rows, num_cols)
        max_comfortable_neighbors = 5
    else:
        assert False

    states_visited = set()

    for i in itertools.count():
        state = tuple(tuple(row) for row in is_occu)
        if state in states_visited:
            break
        states_visited.add(state)

        is_occu2 = [row.copy() for row in is_occu]
        for ind_row in range(num_rows):
            for ind_col in range(num_cols):
                if not is_seat[ind_row][ind_col]:
                    continue

                neighbors_seen = []
                for dx, dy in itertools.product([-1, 0, 1], repeat=2):
                    if dx == 0 and dy == 0:
                        continue
                    for a in range(1, n2):
                        y = ind_row + a*dy
                        x = ind_col + a*dx
                        if 0 <= x < num_cols and 0 <= y < num_rows:
                            if is_seat[y][x]:
                                neighbors_seen.append(is_occu[y][x])
                                break

                num_neighbors = sum(neighbors_seen)
                if not is_occu[ind_row][ind_col] and num_neighbors == 0:
                    is_occu2[ind_row][ind_col] = True
                elif is_occu[ind_row][ind_col] and num_neighbors >= max_comfortable_neighbors:
                    is_occu2[ind_row][ind_col] = False

        is_occu = is_occu2
    else:
        assert False

    return sum(sum(row) for row in is_occu)


res_a = calc_seating(ss, 'a')
print('solution a:', res_a)


res_b = calc_seating(ss, 'b')
print('solution b:', res_b)
