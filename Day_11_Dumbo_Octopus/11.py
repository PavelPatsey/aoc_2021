INPUT = "test_input"


def flash_octopus(octopuses, i, j):
    N = len(octopuses[0])
    octopuses[i][j] = -1
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (
                0 <= i + x <= N - 1
                and 0 <= j + y <= N - 1
                and not (octopuses[i + x][j + y] == -1)
            ):
                octopuses[i + x][j + y] += 1
    return octopuses


def get_flashed_number(octopuses):
    pass


def get_not_flashed_octopus_indexes(octopuses):
    N = len(octopuses[0])
    for i in range(N):
        for j in range(N):
            if octopuses[i][j] >= 9:
                return i, j
    return False


def flash(octopuses):
    octopuses = [[y + 1 for y in x] for x in octopuses]

    indexes = get_not_flashed_octopus_indexes(octopuses)
    while indexes:
        print(indexes)
        octopuses = flash_octopus(octopuses, *indexes)
        indexes = get_not_flashed_octopus_indexes(octopuses)

    return octopuses


def get_flashes_amount(octopuses, steps_number):
    counter = 0
    for _ in range(steps_number):
        octopuses = flash(octopuses)


def read_input():
    with open(INPUT, "r") as file:
        octopuses = [[int(y) for y in x] for x in file.read().split()]
    return octopuses


def main():
    octopuses = read_input()
    print(octopuses)


if __name__ == "__main__":
    assert flash_octopus([[1, 2], [3, 10],], 1, 1) == [
        [2, 3],
        [4, -1],
    ]

    assert (
        get_not_flashed_octopus_indexes(
            [
                [1, 2],
                [3, 6],
            ]
        )
        == False
    )
    assert get_not_flashed_octopus_indexes(
        [
            [1, 2],
            [9, 10],
        ]
    ) == (1, 0)

    octopuses_step_0 = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]
    octopuses_step_1 = [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
    ]

    assert flash(octopuses_step_0) == octopuses_step_1

    main()
