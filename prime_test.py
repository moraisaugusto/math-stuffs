#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i*i) <= n:
        if n % i == 0 or n % (i + 2) == 2:
            return False
        i = i + 6
    return True


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n', help='must be a integer')
args = parser.parse_args()

print('Is {} prime number? {}'.format(args.n, is_prime(int(args.n))))
