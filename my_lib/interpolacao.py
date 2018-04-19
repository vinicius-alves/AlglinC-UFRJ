# -*- coding: utf-8 -*-

from .metodos_basicos import *

#Exercício 1

def interpolacao_polinomial(array_X, array_Y):

	if(len(array_X) != len(array_Y)):
		raise ArithmeticError("array_X e array_Y têm dimensões distintas")

	numero_pontos = len(array_X)

	lista_matriz_P = []

	for i in range(numero_pontos):
		lista_matriz_P.append(np.power(array_X, i))

	matriz_P = transposta(criar_matriz(lista_matriz_P))

	matriz_P_transposta = transposta(matriz_P)

	matriz_Y = transposta(criar_matriz(array_Y))

	matriz_B = inversa(matriz_P_transposta*matriz_P)*(matriz_P_transposta*matriz_Y)

	return matriz_B


#Exercício 4

def interpolacao_lagrange(array_X, array_Y):

	if(len(array_X) != len(array_Y)):
		raise ArithmeticError("array_X e array_Y têm dimensões distintas")


	lista_fi = []

	numero_pontos = len(array_X)

	polinomio = []
	divisor = 1

	for i in range(numero_pontos):

		for j in range(numero_pontos):
			divisor *= array_X[j] - array_X[i]

		#for j in range(numero_pontos):

		#	coeficiente = 

		#	polinomio.append(coeficiente)

		lista_fi.append(np.poly1d(polinomio))
		polinomio = []
		divisor = 1











def print_polinomio(matriz_B):
	array_B = matriz_B.T.A[0]

	polinomio_string = "\nPolinômio = "

	for i in range(len(array_B)-1,-1,-1):

		if( i != len(array_B)-1):
				polinomio_string += " "

		if(array_B[i]>0):
			polinomio_string += "+"+"%.2f" %array_B[i]
		else:
			polinomio_string += "%.2f" %array_B[i] 

		if(i!=0):
			polinomio_string += "X^"+str(i)


	print polinomio_string + "\n"






