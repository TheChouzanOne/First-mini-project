import random

number = random.randint(1,5000000)

guess = int(input('You have 20 tries to guess a number between 1 and 5000000: '))

guessesLeft = 20

lb = 1 #lowerbound
ub = 5000000 #upperbound

while guessesLeft > 0:
    if number == guess:
        print 'Congratulations! You have won.'
        break
    elif guess > number:
        if guess < ub:
            ub = guess
        print 'The number you are looking for is smaller than that!'
    elif guess < number:
        if guess > lb:
            lb = guess
        print 'The number you are looking for is bigger than that!'
    guessesLeft -= 1
    print 'Guesses left: ' + str(guessesLeft)
    print number      
    guess = int(input('Guess a number between ' + str(lb) + ' ' + str(ub) + ':'))
else:
    print 'Game Over!'

