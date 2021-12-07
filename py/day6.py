# Read file

import pandas as pd

counts = pd.read_csv('E:/Projects/advent2021/data/input_6.txt', header=None).transpose()
counts.columns = ['num']

# Part 1/2

counters = pd.DataFrame({"value": [0, 1, 2, 3, 4, 5, 6, 7, 8]})

t = counts.apply(pd.value_counts)
t['value'] = t.index

initial_state = counters.merge(t, on="value", how="left").fillna(0)


def update_state(state):
    new_fish = state["num"].iloc[0]
    state = state.append(pd.DataFrame({"value": 9, "num": new_fish}, index=[9]))
    state = state.iloc[1:, :]
    state.iloc[6, 1] += new_fish
    state["value"] -= 1
    return state


for i in range(0, 80):
    initial_state = update_state(initial_state)

print(sum(initial_state["num"]))

