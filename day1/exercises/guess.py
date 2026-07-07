import random
ans = random.randint(1, 100)

guess = int(input("Guess a number: "))
while guess != ans:
    # tell them how they did
    if guess > ans:
        print("Too high!")
    elif guess < ans:
        print("Too low!")

    # guess again!
    guess = int(input("Guess a number: "))

print("You won!")
