# -*- coding: utf-8 -*-

from .metodos_basicos import *
from .sistemas_lineares import *

#Exercício 8

pontos = [[1.0,1.0],[2.0,2.5],[3.0,3.5],[4.0,4.3]]

def ajusteEquacao(pontos):

	print "\nMelhor ajusta o conjunto de pontos à equação f(x) = a*ln(x) + b/(x**2+1)\n"

	P = []
	Y = []

	for i in range(len(pontos)):

		x = math.log(pontos[i][0])
		y = 1.0/((pontos[i][0]**2)+1)

		linha = [x,y]

		P.append(linha)

		Y.append([pontos[i][1]])

	P_matriz = criar_matriz(P)
	Y_matriz = criar_array(Y)

	A = np.dot(transposta(P_matriz),P_matriz)
	C = np.dot(transposta(P_matriz),Y_matriz)

	B = resolver_sistema_por_decomposicao_LU(A,C)

	return B