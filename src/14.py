import itertools

with open('input14.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip() # 165 ; -

# ss = \
"""
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip() # - ; 208


num_bits = 36


mask_addr_val_all = []
for s in ss.splitlines():
    s1, s2 = s.split(' = ')
    if s1 == 'mask':
        mask = list(s2)
    else:
        s3, s4 = s1.rstrip(']').split('[')
        assert s3 == 'mem'
        addr = int(s4)
        val = int(s2)
        mask_addr_val_all.append((mask, addr, val))



mem = {}
for mask, addr, val in mask_addr_val_all:
    valb = format(val, '0' + str(num_bits) + 'b')
    valb_new = []
    for m, vb in zip(mask, valb):
        if m in '01':
            vb = m
        valb_new.append(vb)
    val_new = int(''.join(valb_new), 2)
    mem[addr] = val_new

res_a = sum(mem.values())
print('solution a:', res_a)


mem = {}
for mask, addr, val in mask_addr_val_all:
    addrb = list(format(addr, '0' + str(num_bits) + 'b'))
    addrb_pattern = []
    inds_x = []
    for i, (m, va) in enumerate(zip(mask, addrb)):
        if m == '1':
            va = '1'
        elif m == '0':
            pass
        elif m == 'X':
            va = 'X'
            inds_x.append(i)
        else: assert False
        addrb_pattern.append(va)

    for new_x_bits in itertools.product('01', repeat=len(inds_x)):
        addrb_new = addrb_pattern.copy()
        for i, x_bit in enumerate(new_x_bits):
            addrb_new[inds_x[i]] = x_bit
        mem[int(''.join(addrb_new), 2)] = val

res_b = sum(mem.values())
print('solution b:', res_b)
