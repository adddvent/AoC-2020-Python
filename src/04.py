import re

with open('input04.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip() # 2 ; -


required_keys = set('byr iyr eyr hgt hcl ecl pid cid'.split()) - {'cid'}


passport_all = []
for line_group in ss.split('\n\n'):
    passport = {}
    for line in line_group.splitlines():
        for kvstring in line.split():
            k, v = kvstring.split(':')
            passport[k] = v
    passport_all.append(passport)


cnt_valid = 0
for passport in passport_all:
    if required_keys.issubset(passport):
        cnt_valid += 1

res_a = cnt_valid
print('solution a:', res_a)


cnt_valid = 0
for passport in passport_all:

    valid_keys = set()
    for k, v in passport.items():
        if k == 'byr':
            if not (rr := re.fullmatch(r'(\d{4})', v)) or not (1920 <= int(rr[1]) <= 2020):
                continue
        elif k == 'iyr':
            if not (rr := re.fullmatch(r'(\d{4})', v)) or not (2010 <= int(rr[1]) <= 2020):
                continue
        elif k == 'eyr':
            if not (rr := re.fullmatch(r'(\d{4})', v)) or not (2020 <= int(rr[1]) <= 2030):
                continue
        elif k == 'hgt':
            if (rr := re.fullmatch(r'(\d+)cm', v)) and (150 <= int(rr[1]) <= 193):
                pass
            elif (rr := re.fullmatch(r'(\d+)in', v)) and (59 <= int(rr[1]) <= 76):
                pass
            else:
                continue
        elif k == 'hcl':
            if not re.fullmatch(r'#[0-9a-f]{6}', v):
                continue
        elif k == 'ecl':
            if v not in 'amb blu brn gry grn hzl oth'.split():
                continue
        elif k == 'pid':
            if not re.fullmatch(r'[0-9]{9}', v):
                continue
        elif k == 'cid':
            pass
        else:
            assert False

        valid_keys.add(k)

    if required_keys.issubset(valid_keys):
        cnt_valid += 1

res_b = cnt_valid
print('solution b:', res_b)
