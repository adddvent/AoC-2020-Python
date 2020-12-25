import itertools

with open('input25.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
5764801
17807724
""".strip() # 14897079 ; -


public_keys = [int(s) for s in ss.splitlines()]


def iterate_transformed_subject_number(subject_number):
    x = 1
    for loopsize in itertools.count(1):
        x = (x * subject_number) % 20201227
        yield x


def transform_subject_number(subject_number, loop_size):
    ii = iterate_transformed_subject_number(subject_number)
    return next(itertools.islice(ii, loop_size-1, loop_size))


pk_remaining = set(public_keys)
loopsizes_found = {}

for i, x in enumerate(iterate_transformed_subject_number(7)):
    if x in pk_remaining:
        pk_remaining.remove(x)
        loopsizes_found[x] = i + 1
        if len(pk_remaining) == 0:
            break

(pubkey1, loopsize1), (pubkey2, loopsize2) = loopsizes_found.items()

encryption_key_1 = transform_subject_number(pubkey1, loopsize2)

# redundant calculation:
# encryption_key_2 = transform_subject_number(pubkey2, loopsize1)
# assert encryption_key_1 == encryption_key_2


res_a = encryption_key_1
print('solution a:', res_a)


# there is no solution b