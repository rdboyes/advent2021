# Read file

import pandas as pd
import numpy as np

points = pd.read_csv('E:/Projects/advent2021/data/input_5.txt',
                     sep=',|\s->\s', header=None,
                     names=["x1", "y1", "x2", "y2"])

# Part 1

b = np.zeros((1000, 1000))


def draw_line(point_series, board, diagonal=False):
    if point_series.iloc[0] == point_series.iloc[2]:
        draw_from = min(point_series.iloc[1], point_series.iloc[3])
        draw_to = max(point_series.iloc[1], point_series.iloc[3]) + 1
        board[point_series.iloc[0], draw_from:draw_to] += 1
    elif point_series.iloc[1] == point_series.iloc[3]:
        draw_from = min(point_series.iloc[0], point_series.iloc[2])
        draw_to = max(point_series.iloc[0], point_series.iloc[2]) + 1
        board[draw_from:draw_to, point_series.iloc[1]] += 1
    elif diagonal:
        x_step = 1 if point_series.iloc[0] < point_series.iloc[2] else -1
        y_step = 1 if point_series.iloc[1] < point_series.iloc[3] else -1
        for x, y in zip(range(point_series.iloc[0], point_series.iloc[2]+x_step, x_step),
                        range(point_series.iloc[1], point_series.iloc[3]+y_step, y_step)):
            board[x, y] += 1
    return board


for index, line in points.iterrows():
    b = draw_line(line, b)

print(sum(b >= 2).sum())

# Part 2

b = np.zeros((1000, 1000))

for index, line in points.iterrows():
    b = draw_line(line, b, True)

print(sum(b >= 2).sum())
