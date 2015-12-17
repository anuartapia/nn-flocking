#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Boid import *
from Utils import *
from ControlSystem import neuralNetwork
from math import log

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
		net = neuralNetwork()
		for x in xrange(0,self.numAgents):
			position = (random.random(),random.random())
			orientation = normalize((random.random(),random.random()))
			self.swarm.append(Boid(position,orientation,velocity,net))

	def simulate(self,steps,motivation):
		"""
		Main simulation function, receives:
		steps - number of time steps
		motivation - boid's motivation to form swarms (dm), 0->avoid 1->follow
		At end of execution self.positions and self.orientations store the configuration of the
		system (boids in space) at each step of the simulation
		"""
		# Initializes self.positions and self.orientations with zeroes
		self.initConfiguration(steps)
		p = self.positions
		d = self.orientations
		# For each time step
		for t in xrange(0,steps-1):
			# For all boids bi
			for i, bi in enumerate(self.swarm):
				# Find all visible boids to bi, wich sensors detected them and distances to them
				boids, sensors, distances = self.visibleBoids(bi)
				# If there is no boids visible to bi
				if (len(boids) == 0) :
					d[i][t+1] = d[i][t]
					p[i][t+1] = add( p[i][t], scale(self.regularSpeed, d[i][t+1]))
				# There are boids visible to bi
				else :
					# For all boids visible to bi
					for j, bj in enumerate(boids):
						# Calculate new values based on the neural nework
						dij, pij = self.newData(i, t, sensors[j], distances[j], motivation)
						d[i][t+1] = add( d[i][t+1], dij)
						p[i][t+1] = add( p[i][t+1], pij)
					# Take average values to make a decision
					d[i][t+1] = scale( (1/len(boids)), d[i][t+1])
					p[i][t+1] = scale( (1/len(boids)), p[i][t+1])
				bi.orientation = d[i][t+1] 
				bi.position = p[i][t+1]
	
	def initConfiguration(self,steps):
		"""
		Initializes self.positions and self.orientations as n*steps matrixes
		where n=size of swarm and steps=time steps for simulation.
		Each entry of matrixes is a vector (2 elements list)
		At time t=0 both matrixes have boids' initial attributes
		"""
		n = len(self.swarm)
		self.positions = [[(0,0) for y in xrange(steps)] for x in xrange(n)]
		self.orientations = [[(0,0) for y in xrange(steps)] for x in xrange(n)]
		for i, bi in enumerate(self.swarm):
			self.positions[i][0] = bi.position
			self.orientations[i][0] = bi.orientation

	def visibleBoids(self,bi):
		"""
		Returns a list of all boids visible to bi in self.swarm, a list
		with tags indicating wich sensor detected them, and a list with
		the distances to each boid detected
		e.g. boids[k], sensors[k] and distances[k] are the k-th boid detected
		by the sensors[k] sensor at distances[k] distance
		"""
		boids = []
		sensors = []
		distances = []
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
			# Distance bewtween bi and bj
			distance = magnitude(sub(pi,pj))
			# If bj is visible to bi, append bj to boids[], correponding sensor
			# to sensors[] and distance to distances[]
			if isBetween(pi, s0transformed, pj):
				boids.append(bj)
				sensors.append(0)
				distances.append(distance)
			if isBetween(pi, s1transformed, pj):
				boids.append(bj)
				sensors.append(1)
				distances.append(distance)
			if isBetween(pi, s2transformed, pj):
				boids.append(bj)
				sensors.append(2)
				distances.append(distance)
			if isBetween(pi, s3transformed, pj):
				boids.append(bj)
				sensors.append(3)
				distances.append(distance)
			if isBetween(pi, s4transformed, pj):
				boids.append(bj)
				sensors.append(4)
				distances.append(distance)
		return boids, sensors, distances

	def newData(self, i, t, sensor, distance, motivation):
		"""
		Computes new position and orientation of i-th boid in swarm, given:
		t - current time step of simulation
		sensor - numeric indicator of the sensor that detected a boid in its view range
		distance - physical distance to detected boid
		motivation - boid's motivation to form swarms
		"""
		# Calculate sensivity of the seen boid
		sensivity = 1 - log(distance + 1) / log(self.dmax + 1)
		# Inputs to be processed by bi's control system (neural network)
		netInputs = [0,0,0,0,0,motivation]
		# Set sensivity value to corresponding input of the system control
		netInputs[sensor] = sensivity
		# Output of bi's control system
		s = self.swarm[i].decide(netInputs)
		# Compute new orientation of bi, dij
		# Current orientation
		d = self.orientations[i][t]
		# =========
		# Tilting vector
		dm = None
		if s >= 0:
			dm = scale( (1-s), d)
		else:
			dm = scale( (1+s), d)
		# =========
		# New direction
		dij = normalize(add(d, normalize(dm)))
		# New position
		pij = add( self.positions[i][t], scale(self.regularSpeed, dij))
		return dij, pij

if __name__ == '__main__':
	#def __init__(numAgents, dmax, regularSpeed, detectionRadius, view, agility):
	am = AgentsModel(10,0.5,0.5,180,0.5,30)
	for b in am.swarm:
		print "pos: "+str(b.position)+" ori: "+str(b.orientation)+" mag: "+str(magnitude(b.orientation))
	am.simulate(10,0)
	print am.positions
	print "===================="
	print am.orientations
