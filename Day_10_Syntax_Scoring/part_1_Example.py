from functools import reduce

BRACKETS = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def read_input():
    with open("input example", "r") as file:
        data = file.read()
    return data.strip().split("\n")


def get_first_illegal_character(seq):
    stack = []
    for bracket in seq:
        if bracket in "<{[(":
            stack.append(BRACKETS[bracket])
        elif bracket == stack[-1]:
            stack.pop()
        else:
            return bracket
    return


def main():
    data = read_input()
    illegal_charactes = filter(
        lambda x: x != None, map(get_first_illegal_character, data)
    )
    scores = map(lambda x: SCORES[x], illegal_charactes)
    scores_sum = reduce(lambda acc, x: acc + x, scores, 0)
    print(scores_sum)


if __name__ == "__main__":
    main()
