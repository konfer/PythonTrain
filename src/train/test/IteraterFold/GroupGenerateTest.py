# coding:utf-8
#
# def group(seq, size):
#
#     def take(seq, n):
#
#         for i in xrange(n):
#             yield seq.next()
#
#     if not hasattr(seq, 'next'):
#             seq = iter(seq)
#
#     while True:
#         x = list(take(seq, size))
#
#         if x:
#             yield x
#         else:
#             break
#
# print list(group([1,2,3,4,8,9,10],2))

def myGroupIter(myList,size):

    def take(iterList,n):
        for i in xrange(n):
            yield iterList.next()

    if not hasattr(myList,"next"):
        myList=iter(myList)

    while True:
        x=list(take(myList,size))

        if x:
            yield x
        else :
            break

print list(myGroupIter([1,2,3,4,5,6],3))