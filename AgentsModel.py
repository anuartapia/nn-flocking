#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Boid import *
from Utils import *
import random

class AgentsModel(object):
	"""
	numAgents - number of agents
	regularSpeed - regular speed of each agent (U/s)
	detectionRadius - max radius of view capabilities of each agent (180°)
	view - max length of view of each agent (1000 U)
	agility - max degrees of movement capabilities of each agent (30°)
	"""
	def __init__(self, numAgents, regularSpeed, detectionRadius, view, agility):
		super(AgentsModel, self).__init__()
		self.numAgents = numAgents
		self.regularSpeed = regularSpeed
		self.detectionRadius = detectionRadius
		self.view = view
		self.agility = agility
		self.createSwarm()

	def createSwarm(self):
		"""
		Initializes a list of n=self.numAgents boids and stores it in 
		self.swarm
		Each boid has random position and random orientation, but constant
		velocity given by self.regularSpeed
		"""
		self.swarm = []
		velocity = self.regularSpeed
		for x in xrange(0,self.numAgents):
			position = (random.random(),random.random())
			orientation = normalize((random.random(),random.random()))
			self.swarm.append(Boid(position,orientation,velocity))

	def simulate(self,steps,dmax,motivation):
		"""
		Main simulation function, receives:
		steps - number of time steps
		dmax - maximal distance Dmax up to which objects can be detected within the boid’s visual hemisphere
		motivation - motivation parameter dm
		"""
		for i in xrange(0,steps):
			pass

if __name__ == '__main__':
	am = AgentsModel(10,1,180,1000,30)
	print am.swarm
	for b in am.swarm:
		print b.orientation, magnitude(b.orientation)
