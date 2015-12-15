#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Boid(object):
	"""docstring for Boid"""
	def __init__(self, position, direction, velocity):
		super(Boid, self).__init__()
		self.position = position
		self.direction = direction
		self.velocity = velocity