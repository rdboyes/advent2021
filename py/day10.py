import statistics

with open("E:/Projects/advent2021/data/input_10.txt", "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

open_to_close = {"[": "]", "{": "}", "(": ")", "<": ">"}
points_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}


def check_line(line):
    stack = []
    corrupted = "No"
    points = 0
    for char in line:
        if char in open_to_close.keys():
            stack.append(char)
        else:
            expected = open_to_close.get(stack.pop())
            if char != expected:
                corrupted = expected
                points = points_dict.get(char)
                break
    return corrupted, points, stack


print(sum([check_line(line)[1] for line in lines]))

# Part 2

p2_dict = {'(': 1, '[': 2, '{': 3, '<': 4}


def p2_score(l):
    score = 0
    for i in l:
        score *= 5
        score += p2_dict.get(i)
    return score

print(statistics.median(
    [p2_score(item) for item in [check_line(line)[2][::-1] for line in lines if check_line(line)[0] == "No"]]
))
