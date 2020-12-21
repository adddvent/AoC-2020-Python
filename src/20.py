import numpy as np
import scipy.signal
import itertools
from collections import defaultdict

with open('input20.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".strip() # 20899048083289 ; 273



def read_raw_tile(lines):
    return np.array([[c == '#' for c in row] for row in lines], dtype=np.bool)

tile_dict = {}
for ss1 in ss.split('\n\n'):
    s1, *lines = ss1.splitlines()
    s1a, s1b = s1.split()
    assert s1a == 'Tile'
    tile_id = int(s1b.rstrip(':'))
    tile = read_raw_tile(lines)
    tile_dict[tile_id] = tile


dirs_slices = {
    (-1,  0): ( 0, slice(None)),
    (1,   0): (-1, slice(None)),
    (0,  -1): (slice(None),  0),
    (0,   1): (slice(None), -1),
    }

dirs_all = list(dirs_slices)


border_line_dict = defaultdict(set)


def iter_tile_transformations(tile):
    for rot in range(2):
        tile2 = np.rot90(tile, rot)
        for flipud in [False, True]:
            tile3 = np.flipud(tile2) if flipud else tile2
            for fliplr in [False, True]:
                tile4 = np.fliplr(tile3) if fliplr else tile3
                yield tile4


tile_trans_dict = defaultdict(list)
for tile_id, tile in tile_dict.items():
    for tile4 in iter_tile_transformations(tile):
        ind_trans = len(tile_trans_dict[tile_id])
        tile_trans_dict[tile_id].append(tile4)

        for dir1, slices1 in dirs_slices.items():
            border_line_dict[(tuple(tile4[slices1]), dir1)].add((tile_id, ind_trans))


# start with any tile (even one that is in the middle) and any transformation
ind_trans = 0
tile_id = list(tile_trans_dict.keys())[0]

r, c = 0, 0
tile_map = {(r, c): (tile_id, ind_trans)}
border = {(r, c)}

while len(border) > 0:
    border_new = set()
    for r, c in border:
        tile_id, ind_trans = tile_map[(r, c)]
        tile = tile_trans_dict[tile_id][ind_trans]
        for (dr, dc), slices1 in dirs_slices.items():
            r2, c2 = r + dr, c + dc
            if (r2, c2) in tile_map:
                continue
            border_vals = tuple(tile[slices1])
            dir2 = (-dr, -dc)
            for tile_id_neighbor, ind_trans_neighbor in border_line_dict[(border_vals, dir2)]:
                if tile_id_neighbor == tile_id:
                    continue
                tile_map[(r2, c2)] = (tile_id_neighbor, ind_trans_neighbor)
                border_new.add((r2, c2))
    border = border_new

r_off, c_off = min(tile_map)
num_rows, num_cols = (z2 - z1 + 1 for z2, z1 in zip(max(tile_map), (r_off, c_off)))

res_a = 1
for r, c in itertools.product([r_off, r_off + num_rows - 1], [c_off, c_off + num_cols - 1]): # for each corner
    res_a *= tile_map[r, c][0]


print('solution a:', res_a)


list_of_rows = []
for ind_r in range(num_rows):
    row = []
    for ind_c in range(num_cols):
        tile_id, ind_trans = tile_map[ind_r + r_off, ind_c + c_off]
        row.append(tile_trans_dict[tile_id][ind_trans][1:-1, 1:-1])
    list_of_rows.append(np.concatenate(row, axis=1))
img = np.concatenate(list_of_rows, axis=0).astype(np.int32)


monster_raw = \
"""
..................#.
#....##....##....###
.#..#..#..#..#..#...
""".strip()

monster = read_raw_tile(monster_raw.splitlines())
num_fields_monster = np.sum(monster)

img2 = img.copy()

for kernel in iter_tile_transformations(monster.astype(np.int32)):
    corr_res = scipy.signal.correlate2d(img, kernel, 'valid') == num_fields_monster
    row_inds, col_inds = np.nonzero(corr_res)
    if len(row_inds) > 0:
        for r, c in zip(row_inds, col_inds):
            img2[r:r+kernel.shape[0], c:c+kernel.shape[1]] &= ~kernel # erase monster pixels

res_b = np.sum(img2)

print('solution b:', res_b)
