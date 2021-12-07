# Read File

txt_file = open('E:/Projects/advent2021/data/input_7.txt', "r")
data = list(map(int, txt_file.read().split(',')))

# Part 1

distances_p1 = map(sum, ([[abs(i - place) for i in data] for place in range(min(data), max(data))]))
print(min(distances_p1))

# Part 2


def crab_distance(i, place):
    dist = abs(i - place)
    if dist <= 1:
        cost = dist
    else:
        cost = sum(range(1, dist+1))
    return cost


distances_p2 = map(sum, ([[crab_distance(i, place) for i in data] for place in range(min(data), max(data))]))
print(min(distances_p2))
