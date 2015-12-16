#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Boid import *
from Utils import *
import random

class AgentsModel(object):
	"""
	numAgents - number of agents
	dmax - maximal distance Dmax up to which objects can be detected within the boid’s visual hemisphere
	regularSpeed - regular speed of each agent (U/s)
	detectionRadius - max radius of view capabilities of each agent (180°)
	view - max length of view of each agent (1000 U)
	agility - max degrees of movement capabilities of each agent (30°)
	"""
	def __init__(self, numAgents, dmax, regularSpeed, detectionRadius, view, agility):
		super(AgentsModel, self).__init__()
		self.numAgents = numAgents
		self.dmax = dmax
		self.regularSpeed = regularSpeed
		self.detectionRadius = detectionRadius
		self.view = view
		self.agility = agility
		# List with all boids in the simulation
		self.swarm = None
		self.createSwarm()
		# Matrix that stores boids' position in a given time of the simulation
		# [i][t] = i-boid's position at t time
		self.positions = None
		# Matrix that stores boids' orientation in a given time of the simulation
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

	def simulate(self,steps,motivation):
		"""
		Main simulation function, receives:
		steps - number of time steps
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
					p[i][t+1] = p[i][t] + self.regularSpeed * d[i][t+1]
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
		Initializes self.positions and self.orientations as n*steps matrixes
		where n=size of swarm and steps=time steps for simulation
		At time t=0 both matrixes have boids' initial attributes
		"""
		n = len(self.swarm)
		self.positions = [[0 for y in xrange(steps)] for x in xrange(n)]
		self.orientations = [[0 for y in xrange(steps)] for x in xrange(n)]
		for i, bi in enumerate(self.swarm):
			self.positions[i][0] = bi.position
			self.orientations[i][0] = bi.orientation

	def visibleBoids(self,bi):
		"""
		Returns a list of all boids visible to bi in self.swarm, paired
		with tags indicating wich sensor detected them
		eg [[bj,0],[bk,3]] means bj was detected by s0 and bk was detected
		by s3
		Also appends the distance to each boid
		"""
		visibles = []
		pi = bi.position
		# Determine the five vectors representing boid's sensors (eyes)
		# North (straigth) sensor
		s2 = bi.orientation
		##ox = bi.orientation[0] # x component of boid's current orientation
		##oy = bi.orientation[1] # y component of boid's current orientation
		# West sensor
		##s0 = (-oy,ox)
		s0 = (-s2[1],s2[0])
		# East sensor
		s4 = (-s0[0],-s0[1])
		# North-west sensor
		s1 = normalize(add(s0,s2))
		# North-east sensor
		s3 = normalize(add(s2,s4))
		# Position end point sensors in relative place to boid and extended to maximal distance of detection
		s0transformed = add(pi, scale(self.dmax,s0))
		s1transformed = add(pi, scale(self.dmax,s1))
		s2transformed = add(pi, scale(self.dmax,s2))
		s3transformed = add(pi, scale(self.dmax,s3))
		s4transformed = add(pi, scale(self.dmax,s4))
		# Check all boids in swarm
		for j, bj in enumerate(self.swarm):
			pj = bj.position
			# If bj appears in any of the sensors, append it to visibles
			#if isBetween(pi, s0transformed, pj): isBetween(pi, s1transformed, pj) or isBetween(pi, s2transformed, pj) or isBetween(pi, s3transformed, pj) or isBetween(pi, s4transformed, pj) :
			#	visibles.append(bj)
			distance = magnitude(sub(pi,pj))
			if isBetween(pi, s0transformed, pj):
				visibles.append( [bj, 0, distance] )
			if isBetween(pi, s1transformed, pj):
				visibles.append( [bj, 1, distance] )
			if isBetween(pi, s2transformed, pj):
				visibles.append( [bj, 2, distance] )
			if isBetween(pi, s3transformed, pj):
				visibles.append( [bj, 3, distance] )
			if isBetween(pi, s4transformed, pj):
				visibles.append( [bj, 4, distance] )
		return visibles


if __name__ == '__main__':
	am = AgentsModel(10,1,180,1000,30)
	print am.swarm
	for b in am.swarm:
		print "pos: "+str(b.position)+" ori: "+str(b.orientation)+" mag: "+str(magnitude(b.orientation))
