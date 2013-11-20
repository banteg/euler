#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''
import time

start = time.clock()

sum = 0
for i in xrange(1, 1001):
    sum += i**i

print str(sum)[-10:]

print time.clock()-start
