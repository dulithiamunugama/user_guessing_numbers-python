import random
num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10 : "))
while num != guess:
    if num > guess:
        print("Too low")
    elif num < guess:
        print("Too high")
    guess = int(input("Guess a number between 1 and 10 : "))
print("congrats! You guessed the correct number.🥳")
