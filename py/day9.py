import pandas as pd
import numpy as np
from igraph import *
from collections import Counter

heights = pd.read_fwf('E:/Projects/advent2021/data/input_9.txt', header=None, widths=[1]*100)

# Part 1

adj = np.apply_along_axis(
    min,
    axis=2,
    arr=np.stack([
            heights.shift(1, fill_value=11),
            heights.shift(-1, fill_value=11),
            heights.shift(1, axis=1, fill_value=11),
            heights.shift(-1, axis=1, fill_value=11)
        ], axis=2)
)

print(np.where(heights < adj, heights + 1, 0).sum())

# Part 2

g = Graph.Lattice(dim=[100, 100], circular=False)
g.vs["height"] = [item for sublist in heights.values.tolist() for item in sublist]
print(Counter(g.subgraph(g.vs.select(height_lt=9)).clusters().membership))

