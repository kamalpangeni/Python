# A simple guessing game. Good practice of
# while else loop for beginners
# done as part of codecademy project
from random import randint

random_num = randint(1,10)

guess_left = 3

while guess_left>0:
    guess=int(input("Guess a number between 1 and 10: "))
    print("You guessed:"+ str(guess))
    if guess > 10 or guess < 0:
        print("Your guess is outside the range!Try again")
        guess = int(input("Guess a number between 1 and 10: "))
    else:
        if guess==random_num:
            print("You Win!")
            break
        else:
            if guess_left!=1:
                print("Try Again!")
            guess_left -= 1
else:
    print("You lose. The correct guess is: "+str(random_num))