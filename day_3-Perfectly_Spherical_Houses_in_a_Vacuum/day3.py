def part_one():
    with open("./input.txt", "r") as f:
        data = f.read()

    coordinates_visited = [(0, 0)]  # (x, y)

    for i in data:
        last = coordinates_visited[-1]
        if i == "v":
            coordinates_visited.append((last[0], last[1] - 1))
        elif i == "^":
            coordinates_visited.append((last[0], last[1] + 1))
        elif i == ">":
            coordinates_visited.append((last[0] + 1, last[1]))
        elif i == "<":
            coordinates_visited.append((last[0] - 1, last[1]))

    return len(set(coordinates_visited))


def part_two():
    with open("./input.txt", "r") as f:
        data = f.read()

    santa_visited = [(0, 0)]
    robo_visited = [(0, 0)]

    for idx, i in enumerate(list(data)):
        last_santa = santa_visited[-1]
        last_robo = robo_visited[-1]

        if i == "v":
            match idx % 2:
                case 0:
                    santa_visited.append((last_santa[0], last_santa[1] - 1))
                case 1:
                    robo_visited.append((last_robo[0], last_robo[1] - 1))
        elif i == "^":
            match idx % 2:
                case 0:
                    santa_visited.append((last_santa[0], last_santa[1] + 1))
                case 1:
                    robo_visited.append((last_robo[0], last_robo[1] + 1))
        elif i == ">":
            match idx % 2:
                case 0:
                    santa_visited.append((last_santa[0] + 1, last_santa[1]))
                case 1:
                    robo_visited.append((last_robo[0] + 1, last_robo[1]))
        elif i == "<":
            match idx % 2:
                case 0:
                    santa_visited.append((last_santa[0] - 1, last_santa[1]))
                case 1:
                    robo_visited.append((last_robo[0] - 1, last_robo[1]))

    return len(set(santa_visited + robo_visited))
