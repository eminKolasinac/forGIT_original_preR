import random

def guess(x):
    random_number = random.randint(1,x)
    #guess = 0


    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry guess again to low")
        elif guess > random_number:
            print(f"guess again too high")
    print(f"yay congrats. You have guessed the number {random_number} correctly")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could be high bc low = high
        feedback = input(f"Is {guess} to high (h), to low (l) or correct (c)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay! Computer guessed your number {guess} correctyly!")
 
 
computer_guess(20)