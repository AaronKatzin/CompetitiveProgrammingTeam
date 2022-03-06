# a simple parser for python. use get_number() and get_word() to read
data = []
def parser():
    global data
    while 1:
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)
            else:
                yield(None)

input_parser = parser()

def get_line():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_line()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

# Program to find third side of triangle using law of cosines
# adapted from https://www.geeksforgeeks.org/program-find-third-side-triangle-using-law-cosines/
 
# Function to calculate cos
# value of angle c
def cal_cos(n):
 
    accuracy = 0.0001
    x1, denominator, cosx, cosval = 0, 0, 0, 0
 
    # Converting degrees to radian
    n = n * (3.142 / 180.0)
 
    x1 = 1
 
    # Maps the sum along the series
    cosx = x1
 
    # Holds the actual value of sin(n)
    cosval = numpy.cos(n)
    i = 1
    while (accuracy <= abs(cosval - cosx)):
 
        denominator = 2 * i * (2 * i - 1)
        x1 = -x1 * n * n / denominator
        cosx = cosx + x1
        i = i + 1
 
    return cosx
 
# Function to find third side
def third_side(a, b, c):
    angle = cal_cos(c)
    return numpy.sqrt((a * a) +
                   (b * b) - 2 * a * b * angle)
 
 # END Program to find third side of triangle using law of cosines

center_to_letter = get_number()
angles = dict()

for i in range(26):
    line = get_line().split(' ')
    angles[line[0]] = float(line[1])

phrase = get_line()

# clean and capitalize phrase:
phrase = ''.join(ch for ch in phrase if ch.isalpha()).upper()

distance = 0.00

for i, letter in enumerate(phrase):
    if i == 0:
        distance += center_to_letter
    else:
        angle = abs(angles[phrase[i-1]] - angles[letter])
        distance_between_letters = third_side(center_to_letter, center_to_letter, angle)
        distance += distance_between_letters
        #print(distance_between_letters)

distance_rounded = int(numpy.ceil(distance))
#print("phrase: ", phrase)
#print("angles: ", angles)
#print("distance: ", distance_rounded)

print(distance_rounded)