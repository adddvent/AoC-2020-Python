from collections import defaultdict

with open('input07.txt', 'rt') as fd:
    ss = fd.read().strip()


# ss = \
"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip() # 4 ; 32


needle = 'shiny gold bag'

parents_dict = defaultdict(list)
bag_dict = {}

for s in ss.splitlines():
    bag_parent, s2 = s.split(' contain ')
    bag_sub_dict = {}
    bag_parent = bag_parent.rstrip('s') # --> '...bag(s)' --> '...bag'
    if s2 != 'no other bags.':
        for s3 in s2.rstrip('.').split(', '):
            num_bags, bag_sub = s3.split(None, 1)
            bag_sub = bag_sub.rstrip('s') # --> '...bag(s)' --> '...bag'
            num_bags = int(num_bags)
            bag_sub_dict[bag_sub] = num_bags
            parents_dict[bag_sub].append(bag_parent)
    bag_dict[bag_parent] = bag_sub_dict



visited = set()
border = {needle}
while len(border) > 0:
    border_new = set()
    for bag in border:
        visited.add(bag)
        border_new |= set(parents_dict[bag]) - visited
    border = border_new

res_a = len(visited - {needle})

print('solution a:', res_a)


def count_inside(bag_dict, bag):
    cnt = 0
    for bag_sub, num_bags in bag_dict[bag].items():
        cnt += num_bags * (1 + count_inside(bag_dict, bag_sub))
    return cnt

res_b = count_inside(bag_dict, needle)

print('solution b:', res_b)
