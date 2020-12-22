from collections import deque

with open('input22.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip() # 306 ; 291


def read_decks(ss):
    deck12 = []
    for ind_player, line_group in enumerate(ss.split('\n\n')):
        deck = []
        for i, s in enumerate(line_group.splitlines()):
            if i == 0:
                assert s == 'Player {}:'.format(ind_player+1)
                continue
            deck.append(int(s))
        deck12.append(deck)
    deck1, deck2 = deck12
    return deck1, deck2


def play_game(deck1, deck2, mode='a'):
    assert mode in 'ab'
    hist = set()
    while len(deck1) > 0 and len(deck2) > 0:
        if mode == 'b':
            he = (tuple(deck1), tuple(deck2))
            if he in hist:
                p1_wins_game = True
                break
            hist.add(he)

        card_p1 = deck1.popleft()
        card_p2 = deck2.popleft()

        if mode == 'b' and len(deck1) >= card_p1 and len(deck2) >= card_p2:
            deck1_sub = deque(list(deck1)[:card_p1])
            deck2_sub = deque(list(deck2)[:card_p2])
            p1_wins_round, _ = play_game(deck1_sub, deck2_sub, mode)
        else:
            p1_wins_round = card_p1 > card_p2

        if p1_wins_round:
            deck1.extend([card_p1, card_p2])
        else:
            deck2.extend([card_p2, card_p1])
    else:
        p1_wins_game = len(deck1) > 0

    return p1_wins_game, (deck1 if p1_wins_game else deck2)


def calc_score(deck):
    return sum((i+1) * v for i, v in enumerate(list(deck)[::-1]))


deck1, deck2 = (deque(deck) for deck in read_decks(ss))

p1wins, deck_winner = play_game(deck1.copy(), deck2.copy(), 'a')
res_a = calc_score(deck_winner)
print('solution a:', res_a)

p1wins, deck_winner = play_game(deck1.copy(), deck2.copy(), 'b')
res_b = calc_score(deck_winner)
print('solution b:', res_b)
