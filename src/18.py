with open('input18.txt', 'rt') as fd:
    ss = fd.read().strip()

# ss = '1 + 2 * 3 + 4 * 5 + 6 ' # 71 ; 231
# ss = '1 + (2 * 3) + (4 * (5 + 6))' # 51 ; 51
# ss = '2 * 3 + (4 * 5)' # 26 ; 46
# ss = '5 + (8 * 3 + 9 + 3 * 4 * 3)' # 437 ; 1445
# ss = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' # 12240 ; 669060
# ss = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2' # 13632 ; 23340



def calc_equation(elems, op_priority_groups, i=0):
    op = None
    ll = []
    all_ops = ''.join(opgroup for opgroup in op_priority_groups)
    n = len(elems)
    while i < n:
        v, i = elems[i], i + 1
        if v == ')':
            break
        elif v == '(':
            y, i = calc_equation(elems, op_priority_groups, i)
        elif isinstance(v, int):
            y = v
        elif v in all_ops:
            op = v
            continue
        else: assert False

        if op is not None:
            ll.append(op)
        ll.append(y)
        op = None

    for ops_to_handle in op_priority_groups:
        ll_new = []
        op = None
        for v in ll:
            if isinstance(v, int):
                if op is None:
                    ll_new.append(v)
                else:
                    if op not in ops_to_handle:
                        ll_new.append(op)
                    elif op == '+': v += ll_new.pop()
                    elif op == '*': v *= ll_new.pop()
                    else: assert False
                    ll_new.append(v)
                    op = None
            elif v in all_ops:
                op = v
            else: assert False
        ll = ll_new

    res, = ll
    return res, i



res_a = 0
res_b = 0
for line in ss.splitlines():
    s_list = line.replace('(', ' ( ').replace(')', ' )').split()
    elems = [int(s) if s.isdecimal() else s for s in s_list]

    res, i = calc_equation(elems, ['+*'])
    res_a += res

    res, i = calc_equation(elems, ['+', '*'])
    res_b += res


print('solution a:', res_a)

print('solution b:', res_b)
