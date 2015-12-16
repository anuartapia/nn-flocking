
import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

if __name__ == "__main__":
	ds = SupervisedDataSet(6, 1)
	# Agregamos muestras al dataset (para el XOR)
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

	net = buildNetwork(6, 7, 1, bias=True)

	try:
		f = open('_learned', 'r')
		net = pickle.load(f)
		f.close()
	except:
		trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
		trainer.trainOnDataset(ds, 1000)
		trainer.testOnData()
		f = open('_learned', 'w')
		pickle.dump(net, f)
		f.close()
	

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