# Read file

import pandas as pd
import numpy as np

winning_nums = pd.read_csv('E:/Projects/advent2021/data/input_4.txt', nrows=1, header=None).transpose()
bingo_boards = pd.read_csv('E:/Projects/advent2021/data/input_4.txt',
                           skip_blank_lines=True, sep='\\s+', skiprows=2, header=None,
                           names=["c1", "c2", "c3", "c4", "c5"])

# Part 1


def transpose_with_names(table):
    t = table.transpose()
    t.columns = ["c1", "c2", "c3", "c4", "c5"]
    return t


winning_nums.columns = ["num"]
winning_nums["time"] = winning_nums.index
order_dict = dict(zip(winning_nums.num, winning_nums.time))

all_wins = pd.concat([bingo_boards,
                      pd.concat(map(lambda m: transpose_with_names(m),
                                np.array_split(bingo_boards, 100)))]).reset_index(drop=True)

numbers_called = all_wins.replace(order_dict).max(axis=1)
numbers_called_for_winner = min(numbers_called)
winning_line = np.argmin(numbers_called)

sum_uncalled = all_wins[all_wins.index // 5 == winning_line // 5] \
    .replace(dict(zip(winning_nums.num[0:numbers_called_for_winner+1], [0]*(numbers_called_for_winner+1)))).sum().sum()

print(sum_uncalled * winning_nums["num"][numbers_called_for_winner])

# Part 2

last_board_to_win = np.argmax(numbers_called.groupby(numbers_called.index % 500 // 5).min())
numbers_called_for_last = numbers_called.groupby(numbers_called.index % 500 // 5).min().max()

sum_uncalled_last = all_wins[all_wins.index // 5 == last_board_to_win] \
    .replace(dict(zip(winning_nums.num[0:numbers_called_for_last+1], [0]*(numbers_called_for_last+1)))).sum().sum()

print(sum_uncalled_last * winning_nums["num"][numbers_called_for_last])
