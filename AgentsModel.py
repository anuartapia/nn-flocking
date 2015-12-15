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
		self.swarm = []
		velocity = 1
		for x in xrange(0,self.numAgents):
			position = (random.random(),random.random())
			direction = normalize((random.random(),random.random()))
			self.swarm.append(Boid(position,direction,velocity))

if __name__ == '__main__':
	am = AgentsModel(10,0.5,180,1000,30)
	print am.swarm
	for b in am.swarm:
		print b.direction, magnitude(b.direction)
