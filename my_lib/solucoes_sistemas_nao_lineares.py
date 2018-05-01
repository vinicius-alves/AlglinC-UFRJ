# -*- coding: utf-8 -*-

from .metodos_basicos import *
import numpy as np

def bissecao(function, a = -10, b = 10, search_a_b = False ,tol = 0.01):

	if(search_a_b):
		while( np.sign(function(a)) + np.sign(function(b)) != 0 ):
			a = np.random.randint(-100,100)
			b = np.random.randint(-100,100)

	else:
		if(np.sign(function(a)) + np.sign(function(b)) != 0):
			raise ArithmeticError("Bisseção não possível: f("+str(a)+") e f("+str(b)+") não possuem sinais opostos")
			

	while(np.abs(b-a)>tol):
		xi = (a+b)/2.0
		fi = function(xi)

		if (fi>0):
			b = xi
		else:
			a = xi

	return xi