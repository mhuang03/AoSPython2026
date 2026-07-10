from random import choice

coin = ["heads", "tails"]

answer = choice(coin)
guess = input("heads or tails? ")

if guess == answer:
    print("You got it!")
else:
    print("You lose.")