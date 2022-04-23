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

def to_dec(symbol):
    global map
    return map.index(symbol)

def getNext_num1():
    global num1
    global map
    for i in range(len(num1)-1, -1, -1):
        yield num1[i]
    while True:
        yield map[0]
def getNext_num2():
    global num1
    global map
    for i in range(len(num2)-1, -1, -1):
        yield num2[i]
    while True:
        yield map[0]

keyLine = get_line()
raw_num1 = get_line()
raw_num2 = get_line()
separator =  get_line()


keys = keyLine.split()
base = int(keys[0])
map = keys[1]
num1 = raw_num1.lstrip()
num2 = raw_num2.lstrip(" +")


#iterate over numbers in reverse
num1_gen = getNext_num1()
num2_gen = getNext_num2()
sum = []
carry = 0
max_len = max(len(num1), len(num2))
for i in range(max_len):
    curr1 = map.index(str(next(num1_gen))) # dec
    curr2 = map.index(str(next(num2_gen))) # dec
    currSum = map[(curr1 + curr2 + carry) % base]  # 'base'
    sum.append(currSum) # building sum list in reverse (as pooposed to concatincating to beginning of non-reversed list) to save complexity 
    carry = (curr1 + curr2 + carry) // base # dec

sum.append(' ')
sum = ''.join(sum)[::-1] # since list was built in reverse, now need to join into string and reverse it back


print(keyLine)
print(raw_num1)
print(raw_num2)
print(separator)
print(sum)