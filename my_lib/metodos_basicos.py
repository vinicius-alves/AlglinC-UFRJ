import sys
import numpy as np
import math

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

def e_positiva_definida(matriz):
	return np.all(np.linalg.eigvals(matriz) > 0)

def valor_polinomio_no_ponto(array_coeficientes, ponto_alvo):
	#array[::-1] inverte a ordem dos elementos do array
	#print   np.poly1d(array_coeficientes[::-1])
	return  np.poly1d(array_coeficientes[::-1])(ponto_alvo)

def submatriz(matriz, cofator):

	B = [[1] * len(matriz) for i in range(len(matriz))]

	for l in range(len(matriz)):
		for k in range(len(matriz)):
			B[l][k] = matriz[l][k]

	B.pop(0)

	for i in range(len(B)):
		B[i].pop(cofator)

	return B

def det(matriz):
    X = 0

    if len(matriz) <= 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    else:
        for i in range(len(matriz)):
            X += matriz[0][i] * ((-1)**i) * det(submatriz(matriz, i))

    return X

def ordenadas_pesos(n):
	return np.polynomial.legendre.leggauss(n)

def array_vazio(n):
	return np.empty(n)