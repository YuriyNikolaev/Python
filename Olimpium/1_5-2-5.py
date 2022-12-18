from math import *
n, a = float(input()), float(input())
ans = (n * pow(a, 2)) / (4 * tan(pi / n))
print(ans)