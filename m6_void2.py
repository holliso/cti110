# void functions vs value returning
# m6
# cti 110
# norrisa
'''
x = int("12")
y = print('test')

print('x is',x)
print('y is',y)
'''

def greet(name):
    """ greets the person called name """
    print('Hello there, ', name)

name = input('What is your name? ')
greet(name)
greet('alice')
greet('steve')

    
def printTwice(something):
    print(something)
    print(something)

printTwice("Hi, I'm Joey Two-Times")
