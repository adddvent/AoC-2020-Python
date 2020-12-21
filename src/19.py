with open('input19.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip() # 2 ; -

# ss = \
"""
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".strip() # - ; 12



def parse_rules_and_patterns(ss):
    rules_pattern_dict = {}
    for s in ss.splitlines():
        s1, s2 = s.split(': ')
        rule_num = int(s1)
        patterns = s2.split(' | ')
        patterns_ored = []
        for patt in patterns:
            if patt.startswith('"') and patt.endswith('"'):
                patterns_ored.append([patt[1:-1]])
            else:
                sub_rules = [int(x) for x in patt.split()]
                patterns_ored.append(sub_rules)
        rules_pattern_dict[rule_num] = patterns_ored
    return rules_pattern_dict


def check_rules(rule_num, rules_pattern_dict, s):
    ll = []
    i = 0
    remaining_rules = [rule_num]
    ll.append((i, remaining_rules))
    while len(ll) > 0:
        i, remaining_rules = ll.pop()
        if len(remaining_rules) == 0:
            if i == len(s):
                break # result found
            else:
                continue

        next_rule = remaining_rules[0]
        if isinstance(next_rule, str):
            if s[i:i+len(next_rule)] == next_rule:
                ll.append((i+len(next_rule), remaining_rules[1:]))
        else:
            for pattern in rules_pattern_dict[next_rule]:
                ll.append((i, pattern + remaining_rules[1:]))
    else:
        return False

    return True



rules_patterns_raw, test_strings_raw = ss.split('\n\n')

rules_pattern_dict = parse_rules_and_patterns(rules_patterns_raw)
test_strings = test_strings_raw.splitlines()


res_a = 0
for s in test_strings:
    found = check_rules(0, rules_pattern_dict, s)
    if found:
        res_a += 1

print('solution a:', res_a)

##

rule_replacements_raw = \
"""
8: 42 | 42 8
11: 42 31 | 42 11 31
""".strip()

rules_pattern_dict.update(parse_rules_and_patterns(rule_replacements_raw))

res_b = 0
for s in test_strings:
    found = check_rules(0, rules_pattern_dict, s)
    if found:
        res_b += 1

print('solution b:', res_b)
