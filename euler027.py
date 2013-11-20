#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
import time

start = time.clock()

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

primes = sieve(13000)

m = (0, 0, 0)
for a in range(-999, 1000):
    for b in xrange(-999, 1000):
        n = 0
        while True:
            q = n**2 + a*n + b
            if q in primes:
                n += 1
            else:
                break
        if n > m[0]:
            m = (n, a, b)
            print m

print m
print m[1]*m[2]

print time.clock()-start
