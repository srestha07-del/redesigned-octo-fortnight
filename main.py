import random as r
number= r.randint(1,100)
attempts=0

print("Guess the number game")
print("HOW TO PLAY : \n 1. I have chosen a number between 1 to 100 \n 2. You have to guess the number using the clues provided:")
print("\t (i) If it says low then it means the actual number is higher than the number you have entered")
print("\t (ii) If it says high then it means the actual number is lower than the number you have entered")

while attempts<5:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low!!!! Try again!!!")
    elif guess > number:
        print("Too high!!! Try again!!!")
    else:
        print("Congratulations! You guessed the number!")
        break

if attempts==5 and guess != number:
    print("Oops! You ran out of attempts. Better luck next time!")

