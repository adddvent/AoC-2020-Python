from collections import deque, defaultdict


ss = '6,4,12,1,20,0,16'

# ss = '0,3,6' # 436 ; 175594
# ss = '1,3,2' # 1 ; 2578
# ss = '3,1,2' # 1836 ; 362



def get_last_spoken(initial_numbers, num_rounds):
    last_spoken = defaultdict(lambda: deque([], 2))

    for i, v in enumerate(initial_numbers):
        last_spoken[v].append(i)

    for i in range(len(initial_numbers), num_rounds):
        if v in last_spoken:
            ls = last_spoken[v]
            if len(ls) < 2:
                v = 0
            else:
                v = ls[1] - ls[0]
        last_spoken[v].append(i)

    return v



initial_numbers = [int(s) for s in ss.split(',')]


res_a = get_last_spoken(initial_numbers, 2020)
print('solution a:', res_a)


# calculating this will take up to 30 seconds
res_b = get_last_spoken(initial_numbers, 30000000)
print('solution b:', res_b)
