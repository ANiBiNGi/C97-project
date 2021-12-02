import random
num = random.randint(1, 9)
chance = 0
print("Number guessing game")
while (chance < 5):
    guess = int(input("Guess the number (between 1 and 9): "))
    if (guess > num):
        print("Not quite there, go lower!")
    elif (guess == num):
        print("Amazing you got it right!")
        break
    else :
        print("Not quite there, go higher!")
    chance += 1
if (chance == 5):
    print("You Lose!!! The number is", num)
