#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def magnitude(v):
	"""
	Returns the euclidean magnitude of v
	"""
	return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

def add(u, v):
	"""
	Returns the vectorial sum of u and v
	"""
	return [ u[i]+v[i] for i in range(len(u)) ]

def sub(u, v):
	"""
	Returns the vectorial sub of u and v
	"""
	return [ u[i]-v[i] for i in range(len(u)) ]

def dot(u, v):
	"""
	Returns the vectorial dot product of u and v
	"""
	return sum(u[i]*v[i] for i in range(len(u)))

def normalize(v):
	"""
	Returns the normalized vetor of v
	"""
	vmag = magnitude(v)
	return [ v[i]/vmag  for i in range(len(v)) ]

def scale(a, u):
	"""
	Scalar product of a and u
	"""
	return [ a*u[i] for i in range(len(u)) ]


def isBetween(u,v,w):
	"""
	Returns true iif w is between u and v in R2
	ie if w is in the segment formed by u and v

	http://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
	"""
	epsilon = 0.001
	crossproduct = (w[1]-u[1])*(v[0]-u[0]) - (w[0]-u[0])*(v[1]-u[1])
	if abs(crossproduct) > epsilon : return False

	dotproduct = dot( sub(v,u), sub(w,u) )
	if dotproduct < 0 : return False

	squaredlengthuv = (v[0]-u[0])*(v[0]-u[0]) + (v[1]-u[1])*(v[1]-u[1])
	if dotproduct > squaredlengthuv : return False

	return True

if __name__ == '__main__':
    l = [1, 2, 3]
    v = [0, 0, 0]

    h = normalize(add(l, v))
    print h
    a = [1,1]
    b = [2,2]
    c = [0.9,0.9]
    isb = isBetween(a,b,c)
    print isb
    w = scale(2.5,l)
    print w