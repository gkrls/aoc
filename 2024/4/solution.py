import os

def find_horizontal(data):
    a = [s.count('XMAS') for s in data]
    b = [s.count('SAMX') for s in data]
    return sum(a) + sum(b)

def find_vertical(data):
    transpose = [''.join([data[r][c] for r in range(len(data))]) for c in range(len(data[0]))]
    return find_horizontal(transpose)

def find_diagonal(s):
    lr = []
    rl = []

    rows = len(s)
    cols = len(s[0])

    # LR diagonals
    for row in range(rows):
        i, j = row, 0
        diag = []
        while i < rows and j < cols:
            diag.append(s[i][j])
            i = i + 1
            j = j + 1
        lr.append(''.join(diag))
    for col in range(1, cols):
        i, j = 0, col
        diag = []
        while i < rows and j < cols:
            diag.append(s[i][j])
            i = i + 1
            j = j + 1
        lr.append(''.join(diag))

    # RL diagonals
    for row in range(rows):
        i, j = row, rows - 1
        diag = []
        while i < rows and j >= 0:
            diag.append(s[i][j])
            i = i + 1
            j = j - 1
        rl.append(''.join(diag))
    for col in range(cols - 2, -1, -1):
        i, j = 0, col
        diag = []
        while i < rows and j >= 0:
            diag.append(s[i][j])
            i = i + 1
            j = j - 1
        rl.append(''.join(diag))

    return find_horizontal(lr) + find_horizontal(rl)

def solution_a(data):
    return find_horizontal(data) + find_vertical(data) + find_diagonal(data)


def solution_b(data):
    res = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == 'A':
                diag = ''.join([data[i - 1][j - 1], data[i - 1][j + 1], data[i + 1][j - 1], data[i + 1][j + 1]])
                if diag == 'MSMS' or diag == 'SMSM' or diag == 'MMSS' or diag == 'SSMM':
                    res = res + 1
    return res


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    data = f.read().splitlines()
    print(solution_a(data))
    print(solution_b(data))