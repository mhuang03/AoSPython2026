# Problem 3: Anagrams
# Design a function that accepts two strings and returns True if the strings are anagrams,
# and False otherwise. Anagrams are words or phrases that are formed by rearranging the
# letters of another word or phrase, using all the original letters exactly once.
# For example, "listen" and "silent" are anagrams.
# Hint: You could: 1) use a dictionary to store the counts of each letter in each string.
#               or 2) sort the letters in each string and compare the sorted strings.

# def count_letters(word):
#     counts = {}
#     for char in word:
#         if char in counts:
#             counts[char] += 1
#         else:
#             counts[char] = 1
#     return counts
#
#
# def anagram(word1, word2):
#     counts1 = count_letters(word1)
#     counts2 = count_letters(word2)
#
#     if len(counts1) != len(counts2):
#         return False
#
#     for char in counts1:
#         if char not in counts2:
#             return False
#         if counts1[char] != counts2[char]:
#             return False
#     return True

def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(anagram("silent", "listen"))