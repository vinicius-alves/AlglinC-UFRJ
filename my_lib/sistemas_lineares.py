from .metodos_basicos import *

#Exercício 1

def decomposicaoLU(matriz):

	if(not(e_quadrada(matriz))):
		raise ArithmeticError("Decomposição LU não aplicável, a matriz não é quadrada")

	if(not(e_nao_singular(matriz))):
		raise ArithmeticError("Decomposição LU não aplicável, a matriz é singular")

	size = matriz.shape[0]
	matriz_L = np.zeros(matriz.shape)
	matriz_U = np.zeros(matriz.shape)

	for i in range(0,size):

		for k in range(i,size):

			soma = 0;
			for j in range(0,i):
				soma += (matriz_L[i][j] * matriz_U[j][k])
			matriz_U[i][k] = matriz.A[i][k] - soma

		for k in range(i,size):
			if(i ==k):
				matriz_L[i][k] =1
			else:
				soma = 0;
				for j in range(0,i):
					soma += (matriz_L[k][j] * matriz_U[j][i])
				matriz_L[k][i] = (matriz.A[k][i] - soma)/matriz_U[i][i]


	return matriz_L, matriz_U


def multiplicacao_retro_substituicao(matriz_L,matriz_B):

	matriz_Y = np.zeros(matriz_L.shape[0])
	num_linhas = matriz_L.shape[0]
	num_colunas = matriz_L.shape[1]

	for i in range(num_linhas):
		if(i==0):
			matriz_Y[i] = matriz_B[i]/matriz_L[i][i]
		else:
			soma = 0
			for j in range(i):
				soma+= (matriz_L[i][j]*matriz_Y[j])

			matriz_Y[i] = (matriz_B[i]- soma)/matriz_L[i][i]

	return matriz_Y


def multiplicacao_substituicao_para_frente(matriz_U, matriz_Y):
	
	matriz_X = np.zeros(matriz_U.shape[0])
	num_linhas = matriz_U.shape[0]
	num_colunas = matriz_U.shape[1]
	
	for i in range(num_linhas-1,-1,-1):

		if(i==num_linhas-1):
			matriz_X[i] = matriz_Y[i]/matriz_U[i][i]
		else:
			soma = 0
			for j in range(i,num_colunas-1):
				soma+= (matriz_U[i][j+1]*matriz_X[j+1])

			matriz_X[i] = (matriz_Y[i]- soma)/matriz_U[i][i]

	return matriz_X

def resolver_sistema_por_decomposicao_LU(matriz_A,matriz_B):

	if(matriz_A.shape[0] != matriz_B.shape[0]):
		raise ArithmeticError("Matriz A e B possuem diferente número de linhas")

	matriz_L, matriz_U = decomposicaoLU(matriz_A)
	matriz_Y = multiplicacao_retro_substituicao(matriz_L,matriz_B)
	matriz_X =  multiplicacao_substituicao_para_frente(matriz_U, matriz_Y)

	return(matriz_X)

def print_array_resposta(matriz_X):

	print("\n")

	for i in range(len(matriz_X)):
		if(i==0):
			if(matriz_X[i]<0):	
				print(" matriz_X = |","%.3f" % matriz_X[i],"|")
			else:
				print(" matriz_X = | ","%.3f" % matriz_X[i],"|")

		else:
			if(matriz_X[i]<0):	
				print("            |","%.3f" % matriz_X[i],"|")
			else:
				print("            | ","%.3f" % matriz_X[i],"|")