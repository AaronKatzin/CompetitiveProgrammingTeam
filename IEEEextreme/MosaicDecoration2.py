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

width =  get_number()
height =  get_number()
tile_width = get_number()
tile_height = get_number()
pile_cost = get_number()
work_cost_per_inch_cut = get_number()

# old tile calculation method using area, failed on 3 hidden tests
# area_to_cover = width * height
# area_per_tile = tile_width * tile_height
# tiles_needed = area_to_cover / area_per_tile

# calculate tiles needed
tiles_for_width = width / tile_width
tiles_for_height = height / tile_height

# round up tiles 
if(tiles_for_width % 1):
    tiles_for_width = tiles_for_width - (tiles_for_width % 1) + 1
if(tiles_for_height % 1):
    tiles_for_height = tiles_for_height - (tiles_for_height % 1 ) + 1

# total
tiles_needed = tiles_for_width * tiles_for_height


#calculate number of piles needed
piles_needed = tiles_needed / 10

# round up
if(piles_needed % 1):
    piles_needed = piles_needed - (piles_needed % 1) + 1

# calculate cut needed
cut_for_height = bool(height % tile_height) * width
cut_for_width = bool(width % tile_width) * height

#print("tiles_needed: ", tiles_needed)
#print("piles_needed: ", piles_needed)
#print("cut_for_height: ", cut_for_height)
#print("cut_for_width: ", cut_for_width)

cost = int(piles_needed * pile_cost + (work_cost_per_inch_cut * (cut_for_height + cut_for_width)))# cutting cost
print(cost)