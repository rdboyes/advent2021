# Read file

import pandas as pd

day3 = pd.read_fwf('E:/Projects/advent2021/data/input_3.txt', header=None, widths=[1]*12)

# Part 1

gamma = day3.mode(axis=0)
epsilon = 1-gamma


def series_to_int(s):

    return int(s.iloc[0].astype(str).str.cat(), base=2)


print(series_to_int(gamma) * series_to_int(epsilon))

# Part 2
oxygen = co2 = 1 - day3.copy()

for i in range(0, 12):
    oxygen = oxygen[oxygen[i] == oxygen.mode(axis=0).values[0, i]]
    if len(oxygen.index) == 1:
        break

for i in range(0, 12):
    co2 = co2[co2[i] == (1 - co2.mode(axis=0).values[0, i])]
    if len(co2.index) == 1:
        break

print(series_to_int(1 - co2) * series_to_int(1 - oxygen))
