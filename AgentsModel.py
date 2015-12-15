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
		# List with all boids in the simulation
		self.swarm = None
		self.createSwarm()
		# Stores boids' position in a given time of the simulation
		# [i][t] = i-boid's position at t time
		self.positions = None
		# Stores boids' orientation in a given time of the simulation
		# [i][t] = i-boid's orientation at t time
		self.orientations = None

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
		At end of execution self.positions and self.orientations store the configuration of the
		system (boids in space) at each step of the simulation
		"""
		# Initializes self.positions and self.orientations
		self.initConfiguration(steps)
		p = self.positions
		d = self.orientations
		# For each time step
		for t in xrange(0,steps):
			# For all boids bi
			for i, bi in enumerate(self.swarm):
				# Find all visible boids to bi
				bjs = self.visibleBoids(bi)
				# If there is no boids visible to bi
				if (len(bjs) == 0) :
					d[i][t+1] = d[i][t]
					p[i][t+1] = d[i][t] + self.regularSpeed * d[i][t+1]
				# There are boids visible to bi
				else :
					d[i][t+1] = 0
					p[i][t+1] = 0
					# For all boids visible to bi
					for j, bj in enumerate(bjs):
						# Calculate new values based on the neural nework
						dij, pij = newData(bi, bj, t)
						d[i][t+1] = d[i][t+1] + dij
						p[i][t+1] = p[i][t+1] + pij
					# Take average values to make a decision
					d[i][t+1] = d[i][t+1] / len(bj)
					p[i][t+1] = p[i][t+1] / len(bj)
				bi.orientation = d[i][t+1] 
				bi.position = p[i][t+1]
	
	def initConfiguration(self,steps):
		"""
		Initializes self.positions and self.orientations
		"""
		n = len(self.swarm)
		self.positions = [[0 for y in xrange(steps)] for x in xrange(n)]
		self.orientations = [[0 for y in xrange(steps)] for x in xrange(n)]
		for i, bi in enumerate(self.swarm):
			self.positions[i][0] = bi.position
			self.orientations[i][0] = bi.orientation


if __name__ == '__main__':
	am = AgentsModel(10,1,180,1000,30)
	print am.swarm
	for b in am.swarm:
		print b.orientation, magnitude(b.orientation)
