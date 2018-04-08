import sys
import numpy as np

def criar_matriz(lista_de_linhas):
	return np.matrix(lista_de_linhas)

def criar_array(lista_de_itens):
	return np.array(lista_de_itens)
	
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