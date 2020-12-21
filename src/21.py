from collections import defaultdict, Counter

with open('input21.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip() # 5 ; mxmxvkd,sqjhc,fvjkl


food_all = []
ingreds_all = set()
allerg_cands = defaultdict(list)
allerg_counts = defaultdict(int)

for s in ss.splitlines():
    s1, s2 = s.split('(contains ')
    ingreds = s1.strip().split()
    allergs = s2.rstrip(')').split(', ')
    food_all.append((ingreds, allergs))
    ingreds_all |= set(ingreds)

    for al in allergs:
        allerg_cands[al].extend(ingreds)
        allerg_counts[al] += 1


found_al_ing = {}

changed = True
while changed:
    changed = False
    for al, ing_cands in allerg_cands.items():
        cc = Counter(ing_cands)
        cands2 = [ing for ing, cnt in cc.items() if cnt == allerg_counts[al] and ing not in found_al_ing.values()]
        if len(cands2) == 1:
            ing_found, = cands2
            assert al not in found_al_ing
            found_al_ing[al] = ing_found
            changed = True


harmless_ingreds = ingreds_all - set(found_al_ing.values())

res_a = 0
for ingreds, allergs in food_all:
    res_a += sum(ing in harmless_ingreds for ing in ingreds)

print('solution a:', res_a)


res_b = ','.join(ing for al, ing in sorted(found_al_ing.items()))

print('solution b:', res_b)
