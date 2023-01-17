# http://codeforces.com/problemset/problem/431/C

"""
Ideas -
1. The max depth I could go to if I was free to choose the path would be n - but because I have to have an edge of weight d in the paths, I can go max to a depth of n-(d-1)
2. At any level x, I have x**k vertices, all of which have access to all numbers below them from 1...k
"""

n, k, d = [int(x) for x in input().split()]
