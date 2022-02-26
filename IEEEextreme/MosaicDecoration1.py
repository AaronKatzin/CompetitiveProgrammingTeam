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

# numpy and scipy are available for use
#import numpy
#import scipy

black_tiles = 0
pink_tiles = 0

n = get_number()
Cb = get_number()
Cp = get_number()

for room in range(n):
    black_tiles += get_number()
    pink_tiles += get_number()
    #print("Room" +  str(room) + ": ", Bi, Pi)

if((black_tiles % 10)):
    black_tiles = black_tiles + (10 - (black_tiles % 10)) # round up to next 10, TODO: deal with 0 case
if((pink_tiles % 10)):
    pink_tiles = pink_tiles + (10 - (pink_tiles % 10)) # round up to next 10, TODO: deal with 0 case

#print("black_tiles: ", black_tiles)
#print("pink_tiles: ", pink_tiles)
#print("black_tile_piles: ", black_tile_piles)
#print("pink_tile_piles: ", pink_tile_piles)


cost = int(((black_tiles / 10) * Cb) + ((pink_tiles / 10) * Cp))

print(cost)
#res = n + b + p
#print(res)