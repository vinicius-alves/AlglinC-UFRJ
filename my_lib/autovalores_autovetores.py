# -*- coding: utf-8 -*-

from .metodos_basicos import *

#Exercício 1

def powerMethod(matriz_A):

	matriz_X_linhas = []
	r = 1

	for i in range(matriz_A.shape[0]):
		matriz_X_linhas.append([1])

	matriz_X = criar_array(matriz_X_linhas)

	lambda0 = matriz_X[0]

	while(r > 0.0001):

		matriz_temp_X = np.dot(matriz_A, matriz_X)
		lambda1 = matriz_temp_X[0]

		matriz_X = matriz_temp_X/lambda1

		r = abs((lambda1-lambda0)/lambda1)

		lambda0 = lambda1

	return lambda0, matriz_X

#Exercício 2

def jacobiMethod(matriz_A):

	if(not(e_simetrica(matriz_A))):
		raise ArithmeticError("O método de Jacobi não aplicável, pois a matriz não é simétrica")	

	matriz_X = np.identity(matriz_A.shape[0])

	tol = 0.0001
	maior_valor = 1
	pos_maior_valor = [0,0]
	angulo = 0
	iteracoes = 0

	while (maior_valor > tol):

		maior_valor = 0
		matriz_P = np.identity(matriz_A.shape[0])

		for i in range(matriz_A.shape[0]):
			for j in range(matriz_A.shape[0]):
				if (i != j):
					if abs(matriz_A.A[i][j]) > maior_valor:
						maior_valor = abs(matriz_A.A[i][j])
						pos_maior_valor = [i, j]					

		i = pos_maior_valor[0]
		j = pos_maior_valor[1]

		if matriz_A.A[i][i] == matriz_A.A[j][j]:	
			angulo = math.pi/4
		else:
			angulo = 0.5*(np.arctan((2*matriz_A.A[i][j])/(matriz_A.A[i][i]-matriz_A.A[j][j])))

		matriz_P[i][i] = math.cos(angulo)	
		matriz_P[i][j] = -math.sin(angulo)
		matriz_P[j][i] = math.sin(angulo)
		matriz_P[j][j] = math.cos(angulo)

		matriz_P_transposta = transposta(matriz_P)

		matriz_A = np.dot(np.dot(matriz_P_transposta, matriz_A), matriz_P)
		matriz_X = np.dot(matriz_X, matriz_P)

		for i in range(matriz_A.shape[0]):
			for j in range(matriz_A.shape[0]):
				if (i != j and abs(matriz_A.A[i][j]) < 0.00000001):
					matriz_A.A[i][j] = 0

		iteracoes += 1			

	print iteracoes
	return matriz_A, matriz_X