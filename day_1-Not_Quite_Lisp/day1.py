# TODO optimize this one
def part_one():
    with open('./input.txt', 'r') as f:
        i = f.read()

    li = sorted(i)
    ups = 0

    for i in li:
        if i == '(':
            ups += 1
        else:
            downs = len(li) - ups

    floor = ups - downs
    return floor

# TODO also optimize this one here :p
def part_two():
    with open('./input.txt', 'r') as f:
        i = f.read()

    li = list(i)
    ups = 0
    downs = 0
    floor = 0
    for idx, i in enumerate(li):
        if floor == -1:
            return idx
        if i == '(':
            ups += 1
            floor += 1
        else:
            downs += 1
            floor -= 1


print(part_two())