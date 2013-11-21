#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
import time

start = time.clock()

l_limit = 1
h_limit = 2000000000

def generator():
    n, e1, e2, e3, s1, s2, s3 = 0, 0, 0, 0, set(), set(), set()
    while e1<h_limit:
        n += 1
        e1 = n*(n+1)/2
        e2 = n*(3*n-1)/2
        e3 = n*(2*n-1)
        if e1>l_limit:
            s1.add(e1)
            s2.add(e2)
            s3.add(e3)
    return s1, s2, s3

tr, pe, he = generator()

for i in tr & pe & pe:
    print i

print time.clock()-start
