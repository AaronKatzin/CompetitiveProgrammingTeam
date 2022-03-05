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

num_of_players = get_number()
player_performances = []

# loop over list of player performance indices, catching input
for performance in range(num_of_players):
    player_performances.append(get_number())

num_of_queries = get_number()

# loop over queries
for query in range(num_of_queries):
    team_performance = get_number()

    # build negative mask
    mask = ~team_performance
    sum = 0
    for performance in player_performances:
        # if none of the masked bits are lit, the performace index can be bitwise 'or'ed without lighting wrong bits 
        if (performance & mask) == 0:
            sum = (sum | performance)
    if sum == team_performance:
        print("YES")
    else:
        print("NO")
