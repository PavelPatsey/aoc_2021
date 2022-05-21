from functools import reduce

BRACKETS = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}

SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def read_input():
    with open("input", "r") as file:
        data = file.read()
    return data.strip().split("\n")


def get_sequence_completion(seq):
    stack = []
    for bracket in seq:
        if bracket in "<{[(":
            stack.append(BRACKETS[bracket])
        elif bracket == stack[-1]:
            stack.pop()
        else:
            return
    return stack


def count_scores(stack):
    score = 0
    while stack:
        score = score * 5 + SCORES[stack.pop()]
    return score


def main():
    data = read_input()
    sequences_completions = filter(
        lambda x: x != None, map(get_sequence_completion, data)
    )
    scores = list(map(count_scores, sequences_completions))
    print(sorted(scores)[len(scores) // 2])
    # 2769449099


if __name__ == "__main__":
    main()
