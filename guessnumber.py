import random
def rand(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry to Low. Try Again")
        elif guess > random_number:
            print("Sorry to High. Try again")
    print(f"Yay you guessed correct.The correct number is {random_number}")


def computer_guess(x):
    low = 0
    high = x
    feedback =''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback =input(f"Is {guess} to High(H) , to Low(L) or Correct(c) : ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! You gussed it correct ,The number is {guess}")
computer_guess(1000)
