import os

def safe(l, skip = None):
    idx  = [i for i in range(len(l)) if i is not skip]

    if len(l) == 1 or l[idx[0]] == l[idx[1]]:
        return 0

    if l[idx[0]] <  l[idx[1]]:
        for i in range(1, len(idx)):
            diff = l[idx[i]] - l[idx[i - 1]]
            if diff < 1 or diff > 3:
                return 0
    else:
        for i in range(1, len(idx)):
            diff = l[idx[i - 1]] - l[idx[i]] 
            if diff < 1 or diff > 3:
                return 0
    return 1


def solution_a(data):
    return sum(list(map(safe, data)))

def solution_b(data):
    unsafe = [l for l in data if not safe(l)]
    new_safe = 0
    for l in unsafe:
        for i in range(len(l)):
            if safe(l, i):
                new_safe = new_safe + 1
                break
    return len(data) - len(unsafe) + new_safe


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    data = list(map(lambda l: list(map(int, l.strip().split())), f.readlines()))
    print(solution_a(data))
    print(solution_b(data))
