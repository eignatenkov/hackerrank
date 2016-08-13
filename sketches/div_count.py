from math import sqrt
from collections import Counter

t = int(input())
questions = [int(input()) for i in range(t)]
max_q = max(questions)

factors = [Counter()]
div_count = [1]

while True:
    n = len(factors) + 1
    for i in range(2, int(sqrt(n))+1):
        if not n % i:
            factors.append(factors[n//i - 1] + Counter({i: 1}))
            break
    if len(factors) < n:
        factors.append(Counter({n: 1}))
    tri_factors = factors[-1] + factors[-2]
    tri_factors[2] -= 1
    tri_div_count = 1
    for degree in tri_factors.values():
        tri_div_count *= degree + 1
    div_count.append(tri_div_count)
    if tri_div_count > max_q:
        break

for q in questions:
    for index, d_c in enumerate(div_count):
        if d_c > q:
            print((index)*(index+1)//2)
            break