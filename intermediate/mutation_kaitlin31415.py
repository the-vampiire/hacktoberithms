from collections import Counter

def mutations(lst):
    c1 = Counter(map(str.lower, lst[0]))
    c2 = Counter(map(str.lower, lst[1]))
    c1.subtract(c2)
    return all(n >= 0 for n in c1.values())


