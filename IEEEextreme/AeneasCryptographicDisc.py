# a simple parser for python. use get_number() and get_word() to read
data = []
def parser():
    global data
    while 1:
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)

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
#import scipy

# Program to find third side of triangle using law of cosines
# adapted from https://www.geeksforgeeks.org/program-find-third-side-triangle-using-law-cosines/
 
# Function to find third side
def third_side(a, b, c):
    angle = numpy.cos(numpy.radians(c))
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
        angle = min(abs(angles[phrase[i-1]] - angles[letter]), abs(360 - abs(angles[phrase[i-1]] - angles[letter])))
        distance_between_letters = third_side(center_to_letter, center_to_letter, angle)
        distance += distance_between_letters
        #print(distance_between_letters)

distance_rounded = int(numpy.ceil(distance))
#print("phrase: ", phrase)
#print("angles: ", angles)
#print("distance: ", distance)

print(distance_rounded)