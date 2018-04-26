# -*- coding: utf-8 -*-

from .metodos_basicos import *

#Exercício 1

def interpolacao_polinomial(array_X, array_Y):

	if(len(array_X) != len(array_Y)):
		raise ArithmeticError("array_X e array_Y têm dimensões distintas")

	if( (len(np.unique(array_X)) != len(array_X)) or (len(np.unique(array_Y)) != len(array_Y)) ):
		raise ArithmeticError("Pontos colineares, interpolação não é possível")

	numero_pontos = len(array_X)

	lista_matriz_P = []

	for i in range(numero_pontos):
		lista_matriz_P.append(np.power(array_X, i))

	matriz_P = transposta(criar_matriz(lista_matriz_P))

	matriz_P_transposta = transposta(matriz_P)

	matriz_Y = transposta(criar_matriz(array_Y))

	matriz_B = inversa(matriz_P_transposta*matriz_P)*(matriz_P_transposta*matriz_Y)

	return matriz_B.T.A[0]


#Exercício 4

def interpolacao_lagrange(array_X, array_Y):

	if(len(array_X) != len(array_Y)):
		raise ArithmeticError("array_X e array_Y têm dimensões distintas")

	if( (len(np.unique(array_X)) != len(array_X)) or (len(np.unique(array_Y)) != len(array_Y)) ):
		raise ArithmeticError("Pontos colineares, interpolação não é possível")

	numero_pontos = len(array_X)

	polinomioIteracao = np.poly1d([1])
	polinomioInterpolacao = np.poly1d([0])
	divisor = 1

	for i in range(numero_pontos):

		for j in range(numero_pontos):
			if(i!=j):
				divisor *= array_X[i] - array_X[j]
 				polinomioIteracao *= np.poly1d([1,- array_X[j]])


		polinomioInterpolacao += polinomioIteracao*(array_Y[i]/float(divisor))

		divisor = 1
		polinomioIteracao = np.poly1d([1])

	return polinomioInterpolacao.c[::-1]
	

# Util

def print_polinomio(array_polinomio):

	polinomio_string = "\nPolinômio = "

	for i in range(len(array_polinomio)-1,-1,-1):

		if( i != len(array_polinomio)-1):
				polinomio_string += " "

		if(array_polinomio[i]>0):
			polinomio_string += "+"+"%.2f" %array_polinomio[i]
		else:
			polinomio_string += "%.2f" %array_polinomio[i] 

		if(i!=0):
			polinomio_string += "X^"+str(i)


	print polinomio_string 






