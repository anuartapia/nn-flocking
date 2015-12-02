#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Boid(object):
	"""docstring for Boid"""
	def __init__(self, position, orientation, velocity):
		super(Boid, self).__init__()
		self.position = position
		self.orientation = orientation
		self.velocity = velocity

pos = ['x','y','z']
ori = ['x','y','z']
vel = 0.5
b = Boid(pos,ori,vel)
print b.position