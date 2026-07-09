# Problem 4: Look and Say
# The look-and-say sequence is a sequence of numbers where each term is generated from the previous term.
# The first term is 1. To generate the next term, read the previous term and count the number of digits in each group of the same digit.
# For example, the first 5 terms are:
# 1, 11, 21, 1211, 111221, 312211
# "one", "one one", "two one(s)", "one two, one one", "one one, one two, two one(s)"
# Write a program that asks the user for a number n and prints the first n terms of the look-and-say sequence.
# Hint: It might be more convenient to work with strings instead of numbers for this problem.

n = int(input("How many terms: "))

term = "1"  # 1211
print(term)

for i in range(1, n):
    next_term = ""

    current_digit = term[0]  # stores the current digit we see in the sequence
    tally = 1  # stores how many times we've seen the current digit in a row

    for digit in term[1:]:
        if digit == current_digit:  # if we see the same digit, increase tally by 1
            tally += 1
        else:  # we saw a different digit next.
            next_term += f"{tally}{current_digit}"
            current_digit = digit
            tally = 1
    next_term += f"{tally}{current_digit}"
    print(next_term)
    term = next_term

