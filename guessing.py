from random import randint
random_number = randint(1,10)
guess = None
while True:
    print("Try and guess a number between 1-10")
    guess = int(input())
    if guess < random_number:
        print("WRONG! That number is too low!")
    elif guess > random_number:
        print("WRONG! That number is too high!")
    else:
        print("Would you like to play again?")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == 'y':
            random_number = randint(1,10)
            guess = None
        else:
            print("Thanks for playing!")
            break