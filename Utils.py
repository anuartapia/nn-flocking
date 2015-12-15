#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

def add(u, v):
    return [ u[i]+v[i] for i in range(len(u)) ]

def sub(u, v):
    return [ u[i]-v[i] for i in range(len(u)) ]

def dot(u, v):
    return sum(u[i]*v[i] for i in range(len(u)))

def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]

if __name__ == '__main__':
    l = [1, 1, 1]
    v = [0, 0, 0]

    h = normalize(add(l, v))
    print h