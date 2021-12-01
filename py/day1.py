import pandas as pd

day1 = pd.read_table('E:/Projects/advent2021/data/input_1.txt', header=None)

print((day1.diff() > 0).values.sum())
print((day1.diff(3) > 0).values.sum())
