#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".

def biggieSize(array):
    for i in range(len(array)):
        if array[i]>0:
            array[i]='big'
    return array
print(biggieSize([-1, 3, 5, -5]))
#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
#  (Note that zero is not considered to be a positive number).
def countPositives(array):
    count = 0;
    for x in array:
        if x >0:
            count+=1
    array[len(array)-1]= count
    return array

print(countPositives([1,6,-4,-2,-7,-2]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sumTotal(array):
    sum = 0;
    for x in array:
        sum+=x
    return sum
print(sumTotal([6,3,-2]))

#Average - Create a function that takes a list and returns the average of all the values.x
def average(array):
    sum = 0
    for x in array:
        sum+=x
    return(sum/len(array))
print(average([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list.
def arrayLength(array):
    return(len(array))
print(arrayLength([37,2,1,-9]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
#  If the list is empty, have the function return False.

def minimum(array):
    if len(array)<0:
        return False
    minInt = array[0]
    for x in array:
        if x<minInt:
            minInt = x
    return minInt
print(minimum([600,80,99,26,3,5]))

#Maximum - Create a function that takes a list and returns the maximum value in the list.
#  If the list is empty, have the function return False.
def maximum(array):
    if len(array)<0:
        return False
    maxInt = array[0]
    for x in array:
        if x>maxInt:
            maxInt = x
    return maxInt
print(maximum([600,80,99,26,3,5]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal,
#  average, minimum, maximum and length of the list.

def ultimateAnalysis(array):
    dictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
    for x in array:
        if dictonary['minimum']>x:
            dictonary['minimum'] = x
        if dictonary['maximun']<x:
            dictonary['maximun'] = x
        dictonary['sumTotal']+= x
        dictonary['average']=dictonary['sumTotal']/len(array)
    return dictonary
print(ultimateAnalysis([1,2,1,2,4,0]))

#Reverse List - Create a function that takes a list and return that list with values reversed.
#  Do this without creating a second list.
#  (This challenge is known to appear during basic technical interviews.)       
def reverseList(array):
    array.reverse()
    return array
print(reverseList([10, 11, 12, 13, 14, 15]))
    
