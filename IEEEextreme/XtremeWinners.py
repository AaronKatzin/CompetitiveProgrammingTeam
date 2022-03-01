# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split('\n'))
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

teams = {
"Team 1": 1,
"Knapsackers @UNT": 2,
"MoraSeekers": 3,
"SurpriseTeam": 4,
"CuSAT": 5,
"DongskarPedongi": 6,
"cofrades": 7,
"viRUs": 8,
"TeamName": 9,
"TeamEPFL1": 10,
"whatevs": 11,
"WildCornAncestors": 12,
"TheCornInTheFields": 13,
"Aurora": 14

}

team = get_word()
print(teams[team])