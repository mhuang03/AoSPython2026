prices = {"apple": 2.50, "orange": 3, "banana": 1}

total = 0

response = input("What would you like to buy? ")
while response != "done":
    if response in prices:
        total += prices[response]
    response = input("What would you like to buy? ")

print(f"Total: ${total:.2f}")