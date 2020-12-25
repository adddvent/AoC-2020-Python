from collections import defaultdict

with open('input24.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".strip() # 10 ; 2208


dirdict = { # direction: (dx, dy)
    'se': (1, -1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'nw': (-1, 1),
    'e': (2, 0),
    'w': (-2, 0),
    }


tiles_dict = defaultdict(bool)

for line in ss.splitlines():
    buf = ''
    x, y = 0, 0
    for c in line:
        s = buf + c
        if s not in dirdict:
            buf = s
        else:
            dx, dy = dirdict[s]
            x, y = x + dx, y + dy
            buf = ''
    assert buf == ''
    tiles_dict[(x, y)] ^= True

res_a = sum(tiles_dict.values())

print('solution a:', res_a)



def get_neighbor_tile_coords(dirdict, xy):
    x, y = xy
    return {(x+dx, y+dy) for dx, dy in dirdict.values()}


num_days = 100
blacktiles = {xy for xy, isblack in tiles_dict.items() if isblack}

for ind_day in range(num_days):
    blacktiles_new = set()

    tiles_to_check = blacktiles.copy()
    for xy in blacktiles:
        tiles_to_check |= get_neighbor_tile_coords(dirdict, xy)

    for xy in tiles_to_check:
        num_neighbors = len(get_neighbor_tile_coords(dirdict, xy) & blacktiles)
        if xy in blacktiles:
            if not (num_neighbors == 0 or num_neighbors > 2):
                blacktiles_new.add(xy)
        else:
            if num_neighbors == 2:
                blacktiles_new.add(xy)

    blacktiles = blacktiles_new

res_b = len(blacktiles)

print('solution b:', res_b)
