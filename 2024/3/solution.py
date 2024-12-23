import os

def parse(s):
    res = []

    c = 0

    def parse_char(s, char):
        nonlocal c
        if c >= len(s):
            return False
        res = s[c] == char
        c = c + 1
        return res

    def parse_num(s):
        nonlocal c
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits_parsed = []
        while s[c] in digits:
            if c >= len(s):
                return None
            digits_parsed.append(s[c])
            c = c + 1
        return int(''.join(digits_parsed))

    while c < len(s):
        if not parse_char(s, 'm'):
            continue
        if not parse_char(s, 'u'):
            continue
        if not parse_char(s, 'l'):
            continue
        if not parse_char(s, '('):
            continue

        a = parse_num(s)
        if a is None:
            continue

        if not parse_char(s, ','):
            continue

        b = parse_num(s)
        if b is None:
            continue

        if not parse_char(s, ')'):
            continue

        res.append((a,b))
    return res


def parse_2(s):
    res = []

    c = 0

    def parse_char(s, char):
        nonlocal c
        if c >= len(s):
            return False
        res = s[c] == char
        c = c + 1
        return res

    def parse_num(s):
        nonlocal c
        if c >= len(s):
            return None
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits_parsed = []
        while s[c] in digits:
            if c >= len(s):
                return None
            digits_parsed.append(s[c])
            c = c + 1
        return int(''.join(digits_parsed)) if len(digits_parsed) else None


    enable = True

    while c < len(s):
        if s[c:].startswith('do()'):
            enable = True
            c += len('do()')

        if s[c:].startswith("don't()"):
            enable = False
            c += len("don't()")

        if not enable:
            c = c + 1
            continue

        if not parse_char(s, 'm'):
            continue
        if not parse_char(s, 'u'):
            continue
        if not parse_char(s, 'l'):
            continue

        if not parse_char(s, '('):
            continue

        a = parse_num(s)
        if a is None:
            continue

        if not parse_char(s, ','):
            continue

        b = parse_num(s)
        if b is None:
            continue

        if not parse_char(s, ')'):
            continue

        res.append((a,b))

    return res


def solution_a(data):
    return sum([op[0] * op[1] for op in parse(data)])

def solution_b(data):
    return sum([op[0] * op[1] for op in parse_2(data)])

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    data = f.read()
    print(solution_a(data))
    print(solution_b(data))