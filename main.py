"""
Coin flipping

Problem:
All n coins are on heads side, first iteration flips every mth coin, there're 999 such iteration, from 2 to 1000.
Find how many coins are on heads.
"""


n = 1001
coins = [0] * n

for i in range(1, n):
    for j in range(0, n, i):
        coins[j] = 1 - coins[j]

print(coins.count(1))  # The solution is found

# Using a dictionary to print the solution
d = {}
for n, m in enumerate(coins):
    if m == 1:
        d[n] = m

# Inserting all the data in a list and finding the sq root of each number
import math 

L = []
for n, m in d.items():
    L.append(math.sqrt(n))
print(L)