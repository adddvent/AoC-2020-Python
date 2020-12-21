with open('input03.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip() # 7 ; 336


grid = [s for s in ss.splitlines()]


def count_hits(grid, dr, dc):
    cnt = 0
    num_cols = len(grid[0])
    for ind_r_step, row in enumerate(grid[::dr]):
        ind_c = (ind_r_step * dc) % num_cols
        cnt += row[ind_c] == '#'
    return cnt


res_a = count_hits(grid, 1, 3)

print('solution a:', res_a)


res_b = 1
for dc, dr in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    res_b *= count_hits(grid, dr, dc)

print('solution b:', res_b)
