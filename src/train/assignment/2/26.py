# utf-8

import random

A = set([random.randint(0, 9) for i in range(0, 9)])

print "Set A:" + str(A)

B = set([random.randint(0, 9) for i in range(0, 9)])

print "Set B:" + str(B)

print "A|B:" + str(A | B )
print "A&B:" + str(A & B)
