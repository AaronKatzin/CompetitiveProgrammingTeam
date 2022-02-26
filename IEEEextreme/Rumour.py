# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

def getDistance(a, b):
    generations_from_a = 0
    generations_from_b = 0

    # parent of each node is floor of node val divided by 2. 
    # So to find common parent we keep "floor dividing" the larger (and therefore lower in tree) node
    while(a != b):
        if a > b:
            a = a >> 1
            generations_from_a += 1
        else:
            b = b >> 1
            generations_from_b += 1
    return generations_from_a + generations_from_b

# numpy and scipy are available for use
#import numpy
#import scipy

lines = get_number()

for line in range(lines):
    a = get_number()
    b = get_number()
    print(getDistance(a, b))