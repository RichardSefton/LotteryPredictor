from Arrays import EuroMillionsArrays as ema
from collections import Counter
from itertools import combinations

# sort through the main numbers draw by draw to get common doubles
def main_number_common_doubles(draws):
    d = Counter()
    for sub in draws:
        if len(draws) < 2:
            continue
        sub.sort()
        for comb in combinations(sub, 2):
            d[comb] += 1

    return d.most_common()

def main_number_common_triplets(draws):
    d = Counter()
    for sub in draws:
        if len(draws) < 3:
            continue
        sub.sort()
        for comb in combinations(sub, 3):
            d[comb] += 1

    return d.most_common()

def lucky_star_common_doubles(draws):
    d = Counter()
    for sub in draws:
        sub.sort()
        for comb in combinations(sub, 2):
            d[comb] += 1

    return d.most_common()