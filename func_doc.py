def printMax(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integer.'''
    x = int(x) # convert to integer, if possible
    y = int(y)
    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

printMax(3,5)
print(printMax.__doc__)