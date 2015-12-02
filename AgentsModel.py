#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Boid

class AgentsModel(object):
	"""
	numAgents - number of agents
	regularSpeed - regular speed of each agent (U/s)
	detectionRadius - max radius of view capabilities of each agent (180°)
	view - max length of view of each agent (1000 U)
	agility - max degrees of movement capabilities of each agent (30°)
	dimensions - physical propertierties of each agent (length U, width U, heigth U)
	"""
	def __init__(self, numAgents, regularSpeed, detectionRadius, view, agility, dimensions):
		super(AgentsModel, self).__init__()
		self.numAgents = numAgents
		self.regularSpeed = regularSpeed
		self.detectionRadius = detectionRadius
		self.view = view
		self.agility = agility
