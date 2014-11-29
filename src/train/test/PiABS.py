import math

flag = 4.0
sumPi = 0
n = 1

while math.fabs(flag / (n + 1)) >= 1e-6:
    sumPi += flag / (2 * n - 1)
    n += 1
    flag = -flag

print sumPi

