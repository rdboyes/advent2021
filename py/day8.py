import pandas as pd
import itertools

letters = pd.read_csv('E:/Projects/advent2021/data/input_8.txt',
                      sep='\s\\|\s', header=None,
                      names=["code_in", "code_out"])
# Part 1
print(letters["code_out"].str.rsplit(pat=' ', n=4, expand=True)
      .applymap(lambda x: len(x) in [2, 3, 4, 7])
      .sum()
      .sum()
      )

# Part 2
wires = {0: [0, 1, 2,    4, 5, 6],
         1: [      2,       5   ],
         2: [0,    2, 3, 4,    6],
         3: [0,    2, 3,    5, 6],
         4: [   1, 2, 3,    5   ],
         5: [0, 1,    3,    5, 6],
         6: [0, 1,    3, 4, 5, 6],
         7: [0,    2,       5   ],
         8: [0, 1, 2, 3, 4, 5, 6],
         9: [0, 1, 2, 3,    5, 6]}

perms = list(itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]))
answer_key = [[[perms[n][i] for i in wires[j]] for j in range(10)] for n in range(5040)]


def decode(input_list, output_list, w, p, key):
    answer = ""
    for i, solution in enumerate(key):
        if set([frozenset(c) for c in solution]) == set([frozenset(c) for c in input_list]):
            answer = p[i]
            break

    rev_wires = {frozenset([answer[i] for i in v]): k for k, v in w.items()}
    answer_list = [rev_wires.get(item) for item in [frozenset(i) for i in output_list]]
    return int(''.join(map(str, answer_list)))


letters["out_value"] = letters.apply(lambda x: decode(x.code_in.split(),
                                                      x.code_out.split(),
                                                      wires,
                                                      perms,
                                                      answer_key),
                                     axis=1)

print(letters["out_value"].sum())
