from random import randint

def StackMaker(discs):
    Stack = [0]
    Stack = Stack * discs
    return Stack

def flip(disc):
    if disc == 0:
        disc = 1
    elif disc == 1:
        disc = 0
    return disc

def DiscFlipper(stack):
    

        
    

stack = StackMaker(5)

