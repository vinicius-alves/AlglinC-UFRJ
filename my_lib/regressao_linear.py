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

		X = np.arange(array_Y[0]-50, array_Y[-1]+50, 0.1)
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

	

