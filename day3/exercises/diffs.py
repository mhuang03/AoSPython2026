diffs = [
    [1, 5, 4, 5, 7]
]

while len(diffs[-1]) > 1:
    current_nums = diffs[-1]
    next_diffs = []

    # calculate and store all diffs
    for i in range(len(diffs[-1]) - 1):
        diff = current_nums[i + 1] - current_nums[i]
        next_diffs.append(diff)

    diffs.append(next_diffs)

print(diffs)