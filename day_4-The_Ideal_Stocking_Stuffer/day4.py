from hashlib import md5


def part_one():
    with open("./input.txt", "r") as f:
        data = f.read()

    counter = 1
    while True:
        data_plus_number = data + str(counter)
        if md5(data_plus_number.encode()).hexdigest().startswith("00000"):
            return counter
        counter += 1


def part_two():
    with open("./input.txt", "r") as f:
        data = f.read()

    counter = 1
    while True:
        data_plus_number = data + str(counter)
        if md5(data_plus_number.encode()).hexdigest().startswith("000000"):
            return counter
        counter += 1


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    x = part_one()
    print(x)
    elapsed = time.perf_counter() - start
    print(f"Executed in {elapsed:0.2f} seconds")
