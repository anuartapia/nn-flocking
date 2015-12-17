#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Atajo para crear una red en una patada
from pybrain.tools.shortcuts import buildNetwork
# Capa con función de activación tangente hiperbólica
from pybrain.structure import TanhLayer
# Clase estándar usada para el aprendizaje supervisado
from pybrain.datasets import SupervisedDataSet
# Clase para ajustar los parámetros de los módulos (pesos) en aprendizaje supervisado, mediante backpropagation
from pybrain.supervised.trainers import BackpropTrainer

# Una red con 2 neuronas en la capa de entrada, 3 en la capa intermedia y 1 en la capa de salida
net = buildNetwork(6,7,1)

# Dataset de entrenamiento que soporta entradas de dos dimensiones y salidas de una dimensión
ds = SupervisedDataSet(6,1)

# Agregamos muestras al dataset (para el XOR)
ds.addSample((1, 0, 0, 0, 0, 0),(.75))
ds.addSample((0, 1, 0, 0, 0, 0),(1))
ds.addSample((0, 0, 1, 0, 0, 0),(1))
ds.addSample((0, 0, 1, 0, 0, 0),(0))
ds.addSample((0, 0, 0, 1, 0, 0),(0))
ds.addSample((0, 0, 0, 0, 1, 0),(.25))
ds.addSample((1, 0, 0, 0, 0, 1),(.25))
ds.addSample((0, 1, 0, 0, 0, 1),(.25))
ds.addSample((0, 0, 1, 0, 0, 1),(.5))
ds.addSample((0, 0, 0, 1, 0, 1),(.75))
ds.addSample((0, 0, 0, 0, 1, 1),(.75))

# Trainer para ajustar la red, recibe la red y el conjunto de entrenamiento
trainer = BackpropTrainer(net,ds)
# Realizamos el entrenamiento hasta la convergencia
print trainer.trainUntilConvergence()

print net.activate([1,0,0,0,0,0]);
print net.activate([0,1,0,0,0,0]);
print net.activate([0,0,1,0,0,0]);
print net.activate([0,0,0,1,0,0]);