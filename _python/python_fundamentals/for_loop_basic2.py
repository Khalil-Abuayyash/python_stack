'''
Biggie Size - Given a list, write a function that
changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
'''
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0 :
            list[i] = "big"
    return list

'''
Count Positives - Given a list of numbers,
create a function to replace the last value with the number of positive values.
(Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
'''
def count_positives(list):
    counter = 0
    for i in range(len(list)):
        if list[i] > 0:
            counter = counter + 1
    list[-1] = counter
    return list
'''
Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7
'''
def sum(list):
    s = 0
    for item in list:
        s = s + item
    return s
'''
Average - Create a function that takes a list and returns the average of all the values.x
Example: average([1,2,3,4]) should return 2.5
'''
def avg(list):
    s = 0
    for item in list:
        s = s + item
    a = s / len(list)
    return a
'''
Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0
'''
def length(list):
    counter = 0
    for i in list:
        counter = counter + 1
    return counter
'''
Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False
'''
def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min
'''
Maximum - Create a function that takes a list and returns the maximum value in the list.
If the list is empty, have the function return False.
Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False
'''
def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for item in list:
        if item > max:
            max = item
    return max
'''
Ultimate Analysis - Create a function that takes a list and returns a dictionary
that has the sumTotal, average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) 
should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
'''
def ulAna(list):
    s = sum(list)
    mx = maximum(list)
    mn = minimum(list)
    av = avg(list)
    size = length(list)
    return {
        'sumTotal': s,
        'average': av,
        'minimum': mn,
        'maximum': mx,
        'length': size
    }
'''
Reverse List - Create a function that takes a list and return that list with values reversed.
Do this without creating a second list.
(This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
'''
def rev(list):
    half = int(len(list)/2)
    for i in range(half):
        j = (i * -1 - 1)
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
    print(list)
