
from random import randint

def GuessingGame():
    rand = randint(1,100)
    print(rand)
    name = input('Hello, welcome to game of guess, what is your name: ')
    guess = 0
    attempts = 0
    while True:
        try:
            guess = int(input('what is your guess: '))
            attempts += 1
        except:
            print('gimme a number')
            #ontinue
        if attempts == 10:
            print('I have no time for this')
            break
        if guess == rand:
            print('good job')
            print('your score: ', attempts, ' guesses')
            break
        elif guess != rand:
            print('do better')
        else:
            print('something else')
        
    print('come again soon')


GuessingGame()
                
                
