# coding:utf-8

test_list = [3, 7, 555, 987, 6, 8, 45]

sortList = sorted(test_list)
print sortList



def binary_search_recu(myList, find, left=0, right=None):
    if right is None:
        right = len(myList) - 1
    if left == right:
        if find == myList[left]:
            return left
        else:
            return -1
    else:
        midPoint = (left + right) / 2
        if find > myList[midPoint]:
            return binary_search_recu(myList, find, midPoint + 1, right)
        else:
            return binary_search_recu(myList, find, left, midPoint)
        
print binary_search_recu(sortList, 8)