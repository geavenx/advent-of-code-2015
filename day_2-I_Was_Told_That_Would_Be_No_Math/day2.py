from typing import List


def part_one() -> int:
    def calculate_paper(dimension: List[str]) -> int:
        l = int(dimension[0])
        w = int(dimension[1])
        h = int(dimension[2])
        largest = max([l, w, h])

        gift = 2 * l * w + 2 * w * h + 2 * h * l

        if h == largest:
            return gift + l * w
        elif w == largest:
            return gift + h * l
        else:
            return gift + w * h

    with open("./input.txt", "r") as f:
        data = f.read()

    data_list = data.split()
    total = 0

    for i in data_list:
        total += calculate_paper(i.split("x"))

    return total


def part_two():
    def calculate_ribbon(dimension: List[str]) -> int:
        l = int(dimension[0])
        w = int(dimension[1])
        h = int(dimension[2])
        largest = max([l, w, h])
        bow = l * w * h

        if h == largest:
            smallest_face = w + w + l + l
        elif w == largest:
            smallest_face = h + h + l + l
        else:
            smallest_face = w + w + h + h

        return smallest_face + bow

    with open("./input.txt", "r") as f:
        data = f.read()

    data_list = data.split()
    total = 0

    for i in data_list:
        total += calculate_ribbon(i.split("x"))

    return total


print(part_two())
