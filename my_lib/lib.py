import sys
import numpy as np

def criar_matriz(lista_de_linhas):
	return np.matrix(lista_de_linhas)
	
def determinante(matriz):
	return np.linalg.det(matriz)
	
def e_inversivel(matriz):
	return np.linalg.cond(matriz) < 1/sys.float_info.epsilon
	
def inversa(matriz):
	return np.linalg.inv(matriz)
	
def e_simetrica(matriz):
	return np.allclose(matriz, matriz.T, atol=1e-8)
	
def transposta(matriz):
	return np.transpose(matriz)