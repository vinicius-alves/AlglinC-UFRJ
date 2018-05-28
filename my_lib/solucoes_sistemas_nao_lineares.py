# -*- coding: utf-8 -*-

from .metodos_basicos import *
import numpy as np
import matplotlib.pyplot as plt
from inspect import getsource

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

def derivada_no_ponto(function,coordenadas,indice_da_variavel, h = 0.00000001):
	#diferenças centrais
	coordenadas_ponto_posterior = list(coordenadas)
	coordenadas_ponto_anterior  = list(coordenadas)

	coordenadas_ponto_posterior[indice_da_variavel] += h
	coordenadas_ponto_anterior [indice_da_variavel] -= h

	f_linha_x = (function(*coordenadas_ponto_posterior) - function(*coordenadas_ponto_anterior))/np.float64(2*h)
	return f_linha_x



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


def metodo_newton_sistemas_nl(functions, num_variaveis, vetor_x = None, tol = 0.0001):

	num_functions    = len(functions)
	matriz_jacobiano = np.zeros((num_functions,num_variaveis), dtype = np.float64)
	matriz_delta_x   = None
	vetor_x_plus_one = None
	tolerancia_R     = 1

	if vetor_x == None or len(vetor_x) != num_variaveis:
		vetor_x = np.ones(num_variaveis) 

	vetor_f = np.ones(num_functions)

	while(tolerancia_R > tol):

		for i in range(num_functions):
			for j in range(num_variaveis):
				matriz_jacobiano[i][j] = derivada_no_ponto(function = functions[i], coordenadas = vetor_x , indice_da_variavel = j)

		for i in range(num_functions):
			vetor_f[i] = functions[i](*vetor_x)
	
		matriz_delta_x = np.dot(inversa(criar_matriz(matriz_jacobiano)),criar_matriz(vetor_f.reshape(-1,1)))* -1
		vetor_delta_x = matriz_delta_x.T.A[0]
		vetor_x_plus_one = vetor_x + vetor_delta_x
		tolerancia_R = np.linalg.norm(vetor_delta_x)/np.linalg.norm(vetor_x_plus_one)
		vetor_x = vetor_x_plus_one
	
	return vetor_x_plus_one
