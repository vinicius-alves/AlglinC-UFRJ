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

def metodo_newton_original(function, tol = 0.0001, ponto_inicial = 10):

	x = ponto_inicial
	tolerancia_R  = 1

	while(tolerancia_R > tol):

		x_plus_one = x - function(x)/derivada_no_ponto(function,coordenadas = [x], indice_da_variavel = 0)
		tolerancia_R = np.abs(x_plus_one-x)
		x = x_plus_one

	return x_plus_one

def metodo_newton_secante(function, tol = 0.0001, ponto_inicial = 10):

	x = ponto_inicial
	x_plus_one = x + 0.001
	tolerancia_R  = 1
	fa = function(x)

	while(tolerancia_R > tol):

		fi = function(x_plus_one)
		x_plus_one = x - fi*(x_plus_one-x)/(fi-fa)
		tolerancia_R = np.abs(x_plus_one-x)
		x = x_plus_one
		fa = fi

	return x_plus_one


def interpolacao_inversa(function, tol = 0.0001, ponto_inicial = 3):

	tolerancia_R = 1

	x0 = 10E+36
	x1 = ponto_inicial 
	x2 = ponto_inicial + 2
	x3 = ponto_inicial + 5

	while(tolerancia_R > tol):

		y1 = function(x1)
		y2 = function(x2)
		y3 = function(x3)

		xk = (y2*y3*x1)/((y1-y2)*(y1-y3)*1.) + (y1*y3*x2)/((y2-y1)*(y2-y3)*1.) + (y1*y2*x3)/((y3-y1)*(y3-y2)*1.)

		tolerancia_R = np.abs(xk-x0)

		if y1>=y2 and y1 >= y3:
			x1 = xk

		elif y2>=y1 and y2 >= y3:
			x2 = xk

		elif y3>=y1 and y3 >= y2:
			x3 = xk

		arr = np.sort([x1,x2,x3])

		x1 = arr[0]
		x2 = arr[1]
		x3 = arr[2]

		
	return xk




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


def metodo_broyden_sistemas_nl(functions, num_variaveis, vetor_x = None, tol = 0.0001):

	num_functions     = len(functions)
	matriz_B          = np.zeros((num_functions,num_variaveis), dtype = np.float64)
	matriz_jacobiano = np.zeros((num_functions,num_variaveis), dtype = np.float64)
	matriz_delta_x    = None
	vetor_x_plus_one  = None
	matriz_B_plus_one = None
	matriz_Y          = None
	matriz_F_plus_one = None
	tolerancia_R      = 1

	if vetor_x == None or len(vetor_x) != num_variaveis:
		vetor_x = np.ones(num_variaveis) 


	for i in range(num_functions):
		for j in range(num_variaveis):
			matriz_jacobiano[i][j] = derivada_no_ponto(function = functions[i], coordenadas = vetor_x , indice_da_variavel = j)

	matriz_B = matriz_jacobiano
	vetor_f = np.ones(num_functions)

	while(tolerancia_R > tol):

		for i in range(num_functions):
			vetor_f[i] = functions[i](*vetor_x)

		matriz_F = criar_matriz(vetor_f.reshape(-1,1))
		matriz_delta_x = - np.dot(inversa(criar_matriz(matriz_B)),matriz_F)

		vetor_delta_x = matriz_delta_x.T.A[0]
		vetor_x_plus_one = vetor_x + vetor_delta_x
		tolerancia_R = np.linalg.norm(vetor_delta_x)/np.linalg.norm(vetor_x_plus_one)

		for i in range(num_functions):
			vetor_f[i] = functions[i](*vetor_x_plus_one)

		matriz_F_plus_one = criar_matriz(vetor_f.reshape(-1,1))
		matriz_Y = matriz_F_plus_one - matriz_F
		matriz_B = criar_matriz(matriz_B)

		matriz_delta_x = criar_matriz(vetor_delta_x).reshape(-1,1)
		divisor = np.power(np.linalg.norm(vetor_delta_x),2)
		matriz_B_plus_one = matriz_B + np.dot(matriz_Y - np.dot(matriz_B,matriz_delta_x),transposta(matriz_delta_x))*(1/np.float(divisor))

		vetor_x = vetor_x_plus_one
		matriz_B = matriz_B_plus_one
	
	return vetor_x_plus_one


def interpolacao_nl(function, pontos_x, pontos_y, num_parametros_b , vetor_b = None, tol = 0.0001):

	num_pontos       = len(pontos_x)
	matriz_jacobiano = np.zeros((num_pontos,num_parametros_b), dtype = np.float64)
	matriz_delta_b   = None
	vetor_b_plus_one = None
	tolerancia_R     = 1
	vetor_f = np.ones(num_pontos)

	if vetor_b == None or len(vetor_b) != num_parametros_b:
		vetor_b = np.ones(num_parametros_b) 

	while(tolerancia_R > tol):
		

		for i in range(num_pontos):
				for j in range(num_parametros_b):
					coords = [pontos_x[i]]+vetor_b
					matriz_jacobiano[i][j] = derivada_no_ponto(function = function, coordenadas = coords, indice_da_variavel = j+1)


		for i in range(num_pontos):
			coords = [pontos_x[i]]+vetor_b
			vetor_f[i] = function(*coords) - pontos_y[i]


		matriz_F = criar_matriz(vetor_f.reshape(-1,1))
		matriz_delta_b = - np.dot(inversa(np.dot(transposta(matriz_jacobiano),matriz_jacobiano)), np.dot(transposta(matriz_jacobiano),matriz_F))
		vetor_delta_b = matriz_delta_b.T.A[0]

		vetor_b_plus_one = vetor_b + vetor_delta_b
		tolerancia_R = np.linalg.norm(vetor_delta_b)/np.linalg.norm(vetor_b_plus_one)
		vetor_b = list(vetor_b_plus_one)
	

	return vetor_b_plus_one
