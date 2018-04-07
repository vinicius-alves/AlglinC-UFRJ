import sys
import numpy as np

def criar_matriz(lista_de_linhas):
	return np.matrix(lista_de_linhas)
	
def determinante(matriz):
	return np.linalg.det(matriz)
	
def e_inversivel(matriz):
	return np.linalg.cond(matriz) < 1/sys.float_info.epsilon

def e_quadrada(matriz):
	return 	matriz.shape[0] == matriz.shape[1]

def e_nao_singular(matriz):
	return e_inversivel(matriz)
	
def inversa(matriz):
	return np.linalg.inv(matriz)
	
def e_simetrica(matriz):
	return np.allclose(matriz, matriz.T, atol=1e-8)
	
def transposta(matriz):
	return np.transpose(matriz)

def decomposicaoLU(matriz):

	if(not(e_quadrada(matriz))):
		raise ArithmeticError("DecomposiçãoLU não aplicável, a matriz não é quadrada")

	if(not(e_nao_singular(matriz))):
		raise ArithmeticError("DecomposiçãoLU não aplicável, a matriz é singular")

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
