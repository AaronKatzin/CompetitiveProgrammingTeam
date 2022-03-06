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
#import numpy

# Function to find third side
# previously function used numpy functions such as sqrt, cos, radian. I replaced them with approximation fomulas based on thes e and pi values
e = 2.718281828459045
pi=3.141592653589793238462643383279
def third_side(center_to_letter, angle):
    angle = angle*(pi/180)
    cos_angle = (e**(angle*1j)).real
    return (2*(center_to_letter**2)- 2*(center_to_letter**2)*cos_angle)**(1/2)

center_to_letter = get_number()
angles = {}

for i in range(26):
    line = get_line().split(' ')
    angles[line[0]] = float(line[1])

phrase = get_line()

# clean and capitalize phrase:
phrase = ''.join(ch for ch in phrase if ch.isalpha()).upper()

# initialize distance as distance from center to first letter
distance = center_to_letter

for i in range(1, len(phrase)):

    angle = min(abs(angles[phrase[i-1]] - angles[phrase[i]]), abs(360 - abs(angles[phrase[i-1]] - angles[phrase[i]])))
    
    # find distance between letters by calculating third side of trianlge using rule of cosines
    distance_between_letters = third_side(center_to_letter, angle)
    distance += distance_between_letters
    #print(distance_between_letters)

distance_rounded = int((-1 * distance)//1) * -1
#print("phrase: ", phrase)
#print("angles: ", angles)
#print("distance: ", distance)

print(distance_rounded)