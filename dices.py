import random
import math

def rollDice(x):
	random.seed()
	return random.randint(1,x)

dice_roll = rollDice(6)

while True:
	guess = input("Please enter a number between 1 and 6: ")

	try:
		player_guess = int(guess)
	except ValueError:
		print("That's not a number!")

print(player_guess)