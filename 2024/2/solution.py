import os

def safe(l):
    if len(l) == 1 or l[0] == l[1]:
        return 0

    if l[0] < l[1]:
        for i in range(1, len(l)):
            diff = l[i] - l[i - 1]
            if diff < 1 or diff > 3:
                return 0
    else:
        for i in range(1, len(l)):
            diff = l[i - 1] - l[i]
            if diff < 1 or diff > 3:
                return 0
    return 1


def solution_a(data):
    return sum(list(map(safe, data)))

def solution_b(data):
    pass

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    data = list(map(lambda l: list(map(int, l.strip().split())), f.readlines()))
    print(solution_a(data))
#     # a = [l[0] for l in ls]
#     # b = [l[1] for l in ls]
#     # print(solution_a(a, b))
#     # print(solution_b(a, b))
