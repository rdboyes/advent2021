# Read file

import pandas as pd
import numpy as np

day2 = pd.read_table('E:/Projects/advent2021/data/input_2.txt', header=None, sep=" ", names=["direction", "value"])

# Part 1

day2["signed_value"] = np.where(day2["direction"] == "up", -day2["value"], day2["value"])

p1_sum_forward = day2[day2["direction"] == "forward"]["signed_value"].sum()
p1_sum_depth = day2[day2["direction"] != "forward"]["signed_value"].sum()

print(p1_sum_forward * p1_sum_depth)

# Part 2

day2["aim_change"] = np.where(day2["direction"] == "forward", 0, day2["signed_value"])
day2["aim"] = day2["aim_change"].cumsum()

p2_sum_forward = day2[day2["direction"] == "forward"]["value"].sum()
p2_sum_depth = (day2[day2["direction"] == "forward"]["signed_value"] * day2[day2["direction"] == "forward"]["aim"]).sum()

print(p2_sum_forward * p2_sum_depth)
