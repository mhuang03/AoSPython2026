# while loops are used to execute a block of code repeatedly as long as a condition is True

# while loop
i = 0
while i < 5:
    print(i)
    i += 1
# prints out the numbers 0 to 4, but when i reaches 5, the loop stops since the condition is no longer True


# break statements can be used to exit a loop before it has completed all its iterations
j = 0
while j < 5:
    print(j)
    if j == 3:
        break
    j += 1
# prints out the numbers 0 to 3, but when j reaches 3, the loop is exited early due to the break statement


# continue statements can be used to skip the rest of the code block and continue to the next iteration of the loop
k = 0
while k < 5:
    k += 1
    if k == 3:
        continue
    print(k)
# prints out the numbers 1, 2, 4, 5, skipping the number 3 due to the continue statement