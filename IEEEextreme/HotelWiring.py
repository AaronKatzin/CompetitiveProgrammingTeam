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

cases = get_number()

for case in range(cases):
    correctly_wired_rooms_per_floor = []
    working_rooms = 0
    floors = get_number()
    rooms_per_floor = get_number()
    switches_off = get_number()
    #print("switches_off: ", switches_off)
    for floor in range(floors):
        correctly_wired_rooms = get_number()
        correctly_wired_rooms_per_floor.append(correctly_wired_rooms)
    #print(correctly_wired_rooms_per_floor)
    correctly_wired_rooms_per_floor.sort()
    #print("[:switches_off]: ", correctly_wired_rooms_per_floor[:switches_off])
    for floor in range(switches_off):
        #print("first loop floor: ", floor)
        working_rooms += (rooms_per_floor - correctly_wired_rooms_per_floor[floor]) * 1
    for floor in range(switches_off, floors):
        #print("second loop floor: ", floor)
        working_rooms += correctly_wired_rooms_per_floor[floor]
    #print("-----> working_rooms: ", working_rooms)
    print(working_rooms)
