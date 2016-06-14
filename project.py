import random

number = random.randint(1,5000000)

guess = int(input('Guess a number between 1 and 5000000: '))

triesLeft = 20

lb = 1
ub = 5000000

while triesLeft > 0:
    if number == guess:
        print 'Congratulations! You won.'
    elif number > guess:
        if guess < ub:
            up = guess
        print 'The number you are looking for is smaller than that!'
    elif number < guess:
        if guess > lb:
            lb = guess
        print 'The number you are looking for is bigger than that!'
    guess = int(input('Guess a number between %s and %s: ' %s (str(lb), str(ub))) 
    triesLeft = triesLeft - 1
else:
    print 'Game Over!'

