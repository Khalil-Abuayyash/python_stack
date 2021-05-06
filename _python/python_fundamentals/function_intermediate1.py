import random
def randInt(max=100, min=0):
    if min > max:
        temp = min
        min = max
        max = temp
    num = random.random()
    num = num * ( max - min ) + min
    num = round(num)
    print(num)
    return num

randInt()
randInt(max=50)
randInt(min=50)
randInt(min=50, max=500)
randInt(max=-20, min=30)