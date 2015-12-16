
import pybrain
# standard class that use the supervised learning for the control sistem of the boids
from pybrain.datasets import *
# Create a neuronal network 
from pybrain.tools.shortcuts import buildNetwork
# Class to adjust the parameters of the modules for the supervised learning through backpropagation
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def neuronalNetwork():
	#We create a supervised data set with six inputs and one output
	ds = SupervisedDataSet(6, 1)
	#We add samples to the data set
	ds.addSample((1, 0, 0, 0, 0, 0),(.75,))
	ds.addSample((0, 1, 0, 0, 0, 0),(1,))
	ds.addSample((0, 0, 1, 0, 0, 0),(1,))
	ds.addSample((0, 0, 1, 0, 0, 0),(0,))
	ds.addSample((0, 0, 0, 1, 0, 0),(0,))
	ds.addSample((0, 0, 0, 0, 1, 0),(.25,))
	ds.addSample((1, 0, 0, 0, 0, 1),(.25,))
	ds.addSample((0, 1, 0, 0, 0, 1),(.25,))
	ds.addSample((0, 0, 1, 0, 0, 1),(.5,))
	ds.addSample((0, 0, 0, 1, 0, 1),(.75,))
	ds.addSample((0, 0, 0, 0, 1, 1),(.75,))
	#We create a network with 6 neurons in the input layer,
	# 7 neurons in the internal layer and one output. we do not wish slant and we use bias = true
	net = buildNetwork(6, 7, 1, bias=True)

	trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
	trainer.trainOnDataset(ds, 1000)
	trainer.testOnData()	

	print net.activate([1,0,0,0,0,0])
	print net.activate([0,1,0,0,0,0])
	print net.activate([0,0,1,0,0,0])
	print net.activate([0,0,1,0,0,0])
	print net.activate([0,0,0,1,0,0])
	print net.activate([0,0,0,0,1,0])
	print net.activate([1,0,0,0,0,1])
	print net.activate([0,1,0,0,0,1])
	print net.activate([0,0,1,0,0,1])
	print net.activate([0,0,0,1,0,1])
	print net.activate([0,0,0,0,1,1])

	return net