# -*- coding: utf-8 -*-

from .metodos_basicos import *
import matplotlib.pyplot as plt

#Exercício 3

def regredir_fx_b1x_b2(array_X, array_Y, exibir_grafico = False):

	'''
	          b2
	f(x) = b1X

	Utilizando ln(y) em ambos os lados:

	ln f(x) = ln(b1) + b2ln(X)

	Podemos escrever g(x) = ln f(x) e b3 = ln(b1)

	Logo o problema se transforma em: g(x) = b3 + ln(b1)
 
	'''

	#matriz_Y carrega g(x) = ln f(x) = ln(array_Y)
	matriz_Y = transposta(criar_matriz(np.log(array_Y)))

	#matriz_P carrega uma coluna de 1s, pois b3 é uma constante, e uma coluna com 
	# fi(x), onde fi é ln, logo será ln(array_X)
	matriz_P = transposta(criar_matriz([np.ones(len(array_X)),np.log(array_X)]))

	matriz_P_transposta = transposta(matriz_P)

	matriz_B = inversa(matriz_P_transposta*matriz_P)*(matriz_P_transposta*matriz_Y)

	#matriz_B possui os valores ótimos para b3 e b2, podemos deduzir b1 pela relação: b1 = exp(b3)
	b2 = np.exp(matriz_B.A[0][0])
	b1 = matriz_B.A[1][0]

	if(exibir_grafico):

		X = np.arange(array_X[0]-50, array_X[-1]+50, 0.1)
		Y = np.zeros(len(X))

		for i in range(len(X)):
			Y[i] = b1* (np.sign(X[i]) * (np.abs(X[i]) ** b2))

		plt.plot(X,Y,"")
		plt.plot(array_X,array_Y,"ro")
		
		plt.title(u"Exercício 3 - regressão f(x) = " + str("%.1f" % b1)+"*X^"+ str("%.1f" % b2))
		plt.ylabel("Y")
		plt.xlabel("X")
		plt.show()

	return b1, b2


#Exercício 5

def regredir_para_polinomio_grau_2(array_X, array_Y, exibir_grafico = False):

	matriz_Y = transposta(criar_matriz(array_Y))
	matriz_P = transposta(criar_matriz([np.ones(len(array_X)),np.power(array_X,1),np.power(array_X,2)]))

	matriz_P_transposta = transposta(matriz_P)

	matriz_B = inversa(matriz_P_transposta*matriz_P)*(matriz_P_transposta*matriz_Y)

	b0 = matriz_B.A[0][0]
	b1 = matriz_B.A[1][0]
	b2 = matriz_B.A[2][0]

	if(exibir_grafico):

		X = np.arange(array_X[0]-5, array_X[-1]+5, 0.1)
		Y = np.zeros(len(X))

		for i in range(len(X)):
			Y[i] = b0 + b1*X[i] + b2*np.power(X[i],2)

		plt.plot(X,Y,"")
		plt.plot(array_X,array_Y,"ro")

		b2_str = str("%.1f" % b2)
		b1_str = "+"+str("%.1f" %b1) if b1 > 0 else str("%.1f" %b1)
		b0_str = "+"+str("%.1f" %b0) if b0 > 0 else str("%.1f" %b0)
	
		
		plt.title(u"Exercício 4 - regressão f(x) = " + b2_str+"*X^2 "+ b1_str+"X^1 " + b0_str)
		plt.ylabel("Y")
		plt.xlabel("X")
		plt.show()


	return matriz_B.T.A[0]


#Exercício 9

def regressaoLinear(pontos):

	somatorio1 = 0
	somatorio2 = 0
	somatorio3 = 0
	somatorio4 = 0
	somatorio5 = 0

	for i in range(len(pontos)):
		somatorio1 += 1
		somatorio2 += pontos[i][0]
		somatorio3 += (pontos[i][0])**2
		somatorio4 += pontos[i][1]
		somatorio5 += pontos[i][0]*pontos[i][1]

	A_linhas = [[somatorio1, somatorio2],[somatorio2, somatorio3]]
	C_linhas = [[somatorio4],[somatorio5]]

	A = criar_matriz(A_linhas)
	C = criar_array(C_linhas)

	B = np.dot(inversa(A),C)

	return B

def pontosUsuario():

	pontos = []
	x = 0
	y = 0

	while(True):

		x = input("Digite o valor de x: ")
		y = input("Digite o valor de y: ")

		ponto = [x,y]

		pontos.append(ponto)

		check = raw_input("Digite Fim para terminar de introduzir pontos; digite qualquer outra coisa para introduzir mais pontos\n")

		if check == "Fim":
			return pontos