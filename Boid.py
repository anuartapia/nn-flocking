#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Boid(object):
	"""
	Simple agent, part of a swarm intelligence simulation
	position - absolute position p ∈ R3 in an unbounded 3D space
	orientation - current orientation which is the present moving direction d ∈ R3 , where |d| = 1
	velocity - current agent velocity v ∈ R
	"""
	def __init__(self, position, orientation, velocity):
		super(Boid, self).__init__()
		self.position = position
		self.orientation = orientation
		self.velocity = velocity
		self.net = None

	def decide(self, netInputs):
		return self.net.activate(netInputs)