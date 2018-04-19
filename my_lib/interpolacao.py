# -*- coding: utf-8 -*-

from .metodos_basicos import *

#Exercício 1

def interpolacao_polinomial(array_X, array_Y):

	if(len(array_X) != len(array_Y)):
		raise ArithmeticError("array_X e array_Y tem dimensões distintas")

	numero_pontos = len(array_X)

	lista_matriz_P = []

	for i in range(numero_pontos):
		lista_matriz_P.append(np.power(array_X, i))

	matriz_P = transposta(criar_matriz(lista_matriz_P))

	matriz_P_transposta = transposta(matriz_P)

	matriz_Y = transposta(criar_matriz(array_Y))

	matriz_B = inversa(matriz_P_transposta*matriz_P)*(matriz_P_transposta*matriz_Y)

	return matriz_B

def print_polinomio(matriz_B):
	array_B = matriz_B.T.A[0]

	polinomio_string = "\nPolinômio = "

	for i in range(len(array_B)-1,-1,-1):

		if( i != len(array_B)-1):
				polinomio_string += " "

		if(i==0):
			if(array_B[i]>0):
				polinomio_string += "+"+"%.2f" %array_B[i]
			else:
				polinomio_string += "%.2f" %array_B[i] 

		else:
			if(array_B[i]>0):
				polinomio_string += "+" + "%.2f" %array_B[i] +"X^"+str(i)

			else:
				polinomio_string += "%.2f" %array_B[i] +"X^"+str(i) 

	print polinomio_string + "\n"






