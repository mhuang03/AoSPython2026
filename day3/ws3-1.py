# Problem 1: Word Count
# Write a program that asks the user for some words, then prints each unique word and
# how many times it appeared.
# Hint: Use a dictionary to store the counts of each word.

text = input("Type some words: ")
words = text.split(" ")

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print("Word count is ")
for word in counts:
    print(word, ":", counts[word])