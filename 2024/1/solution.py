import os

def solution_a(a, b):
    a.sort()
    b.sort()
    c = [abs(a[i] - b[i]) for i in range(len(a))]
    return sum(c)

def solution_b(a, b):
    histo = {}
    for x in b:
        histo[x] = histo.get(x, 0) + 1
    return sum([x * histo.get(x, 0) for x in a])

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    ls = list(map(lambda l: (int(l.split()[0]), int(l.split()[1])), f.readlines()))
    a = [l[0] for l in ls]
    b = [l[1] for l in ls]
    print(solution_a(a, b))
    print(solution_b(a, b))