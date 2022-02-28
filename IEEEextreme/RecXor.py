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

# *Used existing algorithm with Yuval Meir's permission* 
# efficient xor of consecutuve numbers taken from:
# https://www.geeksforgeeks.org/find-xor-of-numbers-from-the-range-l-r/ 

# Python3 implementation of the approach
#from operator import xor
 
# Function to return the XOR of elements
# from the range [1, n]
def findXOR(n):
    mod = n % 4
 
    # If n is a multiple of 4
    if (mod == 0):
        return n
 
    # If n % 4 gives remainder 1
    elif (mod == 1):
        return 1
 
    # If n % 4 gives remainder 2
    elif (mod == 2):
        return n + 1
 
    # If n % 4 gives remainder 3
    elif (mod == 3):
        return 0
 
# Function to return the XOR of elements
# from the range [l, r]
def findXORFun(l, r):
    return (findXOR(l - 1) ^ findXOR(r))

# end of geeksforgeeks existing algorithm

# numpy and scipy are available for use
#import numpy
#import scipy
lines = get_number()

for line in range(lines):
    length = get_number()
    height = get_number()
    start = get_number()
    d1 = get_number()
    d2 = get_number()

    #print(findXORFun(start, d1 - 1) ^ findXORFun(d2 + 1, start - 1 + length*height))

    # find xor of outer rectangle
    outer_xor = findXORFun(start, start - 1 + length*height)

    def getY(num):
        return ((num-start) % length) + 1
    # find xor of inner rectangle
    if getY(d1) < getY(d2) :
    # if ((d1 + start) % length) < ((d2 + start) % length):
        inner_length = getY(d2) - getY(d1) + 1
        inner_start = d1
        inner_end = d2
        #print("if")
    else:
        inner_length = getY(d1) - getY(d2) + 1
        inner_start = d1 - (inner_length - 1)
        inner_end = d2 + (inner_length - 1)
        #print("else")

    inner_height = ((inner_end - inner_start) / length)
    

    #print("inner_height before rounding: ", inner_height)

    if inner_height % 1:
        inner_height = inner_height - (inner_height % 1) + 1
        
    #print("d1: ", d1)
    #print("d2: ", d2)
    #print("inner_length: ", inner_length) 
    #print("inner_start: ", inner_start)
    #print("inner_end: ", inner_end)
    #print("inner_height: ", inner_height)
    
    inner_xor = 0
    row_start = inner_start
    #print("inner_start: ", inner_start)
    #print("inner_end: ", inner_end)
    #print("inner_height: ", inner_height)
    # loop over rows of inner rectangle, xoring each row
    for row in range(int(inner_height)):
        #print("inner row: ", row_start, ", ", row_start + inner_length -1)
        inner_xor = inner_xor ^ findXORFun(row_start, row_start + inner_length - 1)
        row_start += length


    # inner rectangle xor outer rectangle will cancel out the inner xor
    print(outer_xor ^ inner_xor)