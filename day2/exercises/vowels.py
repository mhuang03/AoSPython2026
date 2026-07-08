text = input("Enter a string: ")

vowel_count = 0
for letter in text:
    if letter in "AEIOUaeiou":
        vowel_count += 1

print(f"You typed {vowel_count} vowels!")