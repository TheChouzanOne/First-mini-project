import random

number = random.randint(1,5000000)

guessesLeft = 20

lb = 1 #lowerbound
ub = 5000000 #upperbound


def check_int(n):
    for x in n:
        if x < '0' or x > '9':
            return False
    return True


while guessesLeft > 0:
    
    guess = raw_input('Guess a number between ' + str(lb) + ' ' + str(ub) + ':')
    
    while check_int(guess) == False:
        guess = raw_input('That is not a number, please write it again: ')
    else:
        guess = int(guess)
        
    
    print 'Guesses left: ' + str(guessesLeft)
    
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

    
    print number      
else:
    print 'Game Over!'
   
