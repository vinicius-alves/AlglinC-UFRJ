# -*- coding: utf-8 -*-

from .metodos_basicos import *
import numpy as np
import matplotlib.pyplot as plt
from inspect import getsource
from sympy import *

def visualizar_funcao(function, xmin, xmax, xzero = []):
	array_x = np.arange(xmin,xmax,0.1)
	array_y = function(array_x)

	plt.plot(array_x,array_y)

	if(len(xzero)>0):
		yzero = function(xzero)
		plt.plot(xzero,yzero,"ro")

	plt.title(getsource(function))
	plt.ylabel("f(x)")
	plt.xlabel("x")
	plt.show()

def derivada(function,str_variavel):
	x = Symbol(str_variavel)
	diff = function.diff(x)
	derivada = lambdify(x,diff,'numpy')
	return derivada

def bissecao(function, a = -10, b = 10, search_a_b = False ,tol = 0.01):

	if(search_a_b):
		while( np.sign(function(a)) + np.sign(function(b)) != 0 ):
			a = np.random.randint(-1000,1000)
			b = np.random.randint(-1000,1000)

	else:
		if(np.sign(function(a)) + np.sign(function(b)) != 0):
			raise ArithmeticError("Bisseção não possível: f("+str(a)+") e f("+str(b)+") não possuem sinais opostos")
	
	if(function(a) < function(b)):
		inclinacao_positiva = True
	else:
		inclinacao_positiva = False

	while(np.abs(b-a)>tol):
		xi = (a+b)/2.0
		fi = function(xi)

		if(inclinacao_positiva):

			if (fi>0):
				b = xi
			else:
				a = xi

		else:

			if (fi<0):
				b = xi
			else:
				a = xi

	return xi

