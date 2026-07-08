perfect_count = 0
current_candidate = 1
while perfect_count < 4:
    factor_sum = 0
    for factor in range(1, current_candidate):
        if current_candidate % factor == 0:
            factor_sum += factor
    if factor_sum == current_candidate:
        print(current_candidate)
        perfect_count += 1
    current_candidate += 1