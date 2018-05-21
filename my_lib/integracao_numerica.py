# -*- coding: utf-8 -*-

from .metodos_basicos import *
from .sistemas_lineares import *

#Exercício 1	

def integracao_polinomial(integral):

	pontos_de_integracao = 0
	result = 0
	vandermonde = []
	c = []
	ordenadas = []
	pesos = []

	pontos_de_integracao = input("Insira o número desejado de pontos de integração: ")

	if pontos_de_integracao not in range(1, 11):
		print "O número de pontos deve ser um valor inteiro entre 1 e 10"
		return

	if pontos_de_integracao == 1:
		ordenadas.append((integral[1]+integral[2])/2.0)

	else:
		ordenadas.append(integral[1])

		if pontos_de_integracao == 3:
			ordenadas.append((integral[1]+integral[2])/2.0)

		if pontos_de_integracao > 3:

			delta = (integral[2]-integral[1])/(pontos_de_integracao-1.0)

			for i in range(pontos_de_integracao-2):
				ordenadas.append(integral[1]+(i+1)*delta)

		ordenadas.append(integral[2])

	vandermonde = np.identity(len(ordenadas))
	c = array_vazio(len(ordenadas))

	for i in range(len(ordenadas)):
		for j in range(len(ordenadas)):
			vandermonde[i][j] = ordenadas[j]**i

	vandermonde_matriz = criar_matriz(vandermonde)

	for i in range(len(ordenadas)):
		c[i] = (integral[2]**(i+1.0) - integral[1]**(i+1.0))/(i+1.0)

	pesos = resolver_sistema_por_decomposicao_LU(vandermonde_matriz,c)

	for i in range(pontos_de_integracao):

		result += pesos[i]*integral[0](ordenadas[i])

	return result

def quadratura_Gauss(integral):

	ordenadas = []
	pesos = []
	result = 0

	pontos_de_integracao = input("Insira o número desejado de pontos de integração: ")

	if pontos_de_integracao not in range(1, 11):
		print "O número de pontos deve ser um valor inteiro entre 1 e 10"
		return

	ordenadas, pesos = ordenadas_pesos(pontos_de_integracao)

	print ordenadas
	print pesos

	for i in range(pontos_de_integracao):

		x = 0.5*(integral[1]+integral[2]+((integral[2]-integral[1])*ordenadas[i]))

		result += ((integral[2]-integral[1])/2.0)*(pesos[i]*integral[0](x))

	return result