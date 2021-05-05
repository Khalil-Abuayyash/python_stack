# basic
'''
for num in range(151):
    print(num)
'''

# Multiples of five
'''
for num in range(0,101,5):
    print(num)
'''

# Counting the dojo way
'''
for num in range(101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)
'''

#  whoa that sucjer's huge
'''
sum = 0
for num in range(1,500000,2):
    sum += num
print(sum)
'''

# countdown by fours
'''
for num in range(2018,0,-4):
    print(num)
'''

#  flexible counter
'''
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)
'''