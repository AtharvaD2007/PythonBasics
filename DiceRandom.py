import random

while True:
    choice = input("Roll the dice? (yes/no): ")
    if choice == "yes":
        print("You rolled:", random.randint(1, 6))
    else:
        break