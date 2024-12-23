import os

def order_is_correct(rules, order):
    for i in range(len(order)):
        if order[i] not in rules:
            continue
        for j in range(0, i):
            if order[j] in rules[order[i]]:
                return False
    return True

def solution_a(rules, orders):
    correct_orders = []
    for order in orders:
        if order_is_correct(rules, order):
            correct_orders.append(order)
    return sum([o[len(o) // 2] for o in correct_orders])


def do_correct_order(rules, order):
    while not order_is_correct(rules, order):
        for i in range(len(order)):
            if order[i] not in rules:
                continue
            for j in range(0, i):
                if order[j] in rules[order[i]]:
                    tmp = order[j]
                    order[j] = order[i]
                    order[i] = tmp

def solution_b(rules, orders):
    corrected_orders = []
    for order in orders:
        if not order_is_correct(rules, order):
            do_correct_order(rules, order)
            corrected_orders.append(order)
    return sum([o[len(o) // 2] for o in corrected_orders])

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    data = f.read().split('\n\n')

    rules = {}
    for rule in data[0].splitlines():
        rule = rule.split('|')
        l = int(rule[0])
        r = int(rule[1])
        if l not in rules:
            rules[l] = [r]
        else:
            rules[l].append(r)

    orders = []
    for order in data[1].splitlines():
        orders.append(list(map(int, order.split(','))))

    print(solution_a(rules, orders))
    print(solution_b(rules, orders))