def part_one():
    with open("input.txt", "r") as f:
        data = f.read()

    def is_nice(string: str) -> bool:
        for banned in ["ab", "cd", "xy", "pq"]:
            if banned in string:
                print(f"⛔ [{string}]: contains one of the banned strings ('{banned}')")
                return False

        vowels = sum(string.count(v) for v in "aeiou")
        if vowels < 3:
            print(f"⛔ [{string}]: does not contain at least 3 vowels")
            return False

        has_double = any(string[i] == string[i + 1] for i in range(len(string) - 1))
        if not has_double:
            print(f"⛔ [{string}]: does not contain a letter appearing twice in a row")
            return False

        print(f"✅ [{string}]: is nice!")
        return True

    data_list = data.split()
    nice_strings = 0

    for i in data_list:
        if is_nice(i):
            nice_strings += 1

    print(f"\n✅ FINAL RESULT ✅\nThere are {nice_strings} nice strings in the input!")
    return nice_strings


def part_two():
    with open("input.txt", "r") as f:
        data = f.read()

    def is_nice(string: str) -> bool:
        for banned in ["ab", "cd", "xy", "pq"]:
            if banned in string:
                print(f"⛔ [{string}]: contains one of the banned strings ('{banned}')")
                return False

        vowels = sum(string.count(v) for v in "aeiou")
        if vowels < 3:
            print(f"⛔ [{string}]: does not contain at least 3 vowels")
            return False

        has_double = any(string[i] == string[i + 1] for i in range(len(string) - 1))
        if not has_double:
            print(f"⛔ [{string}]: does not contain a letter appearing twice in a row")
            return False

        print(f"✅ [{string}]: is nice!")
        return True

    data_list = data.split()
    nice_strings = 0

    for i in data_list:
        if is_nice(i):
            nice_strings += 1

    print(f"\n✅ FINAL RESULT ✅\nThere are {nice_strings} nice strings in the input!")
    return nice_strings
