#coding:utf-8
def sum_numbers(numList):
    sum=0
    
    for element in numList:
        if type(element)==list:
            sum+=sum_numbers(element)
        else:
            sum+=element
            
    return sum
    
list1=[2,[5,8,9],3,[3,[7,2]]]

print sum_numbers(list1)