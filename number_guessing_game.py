import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
guessed_correctly = False

while attempts < max_attempts:
  guess = int(input("Enter your guess: "))
  attempts += 1

  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print("Too high! Try again.")
  else:
    print(f"Correct! You guessed it in {attempts} attempts.")
    guessed_correctly = True
    break

if not guessed_correctly:
  print(f"Out of attempts! The number was {secret_number}.")

44
