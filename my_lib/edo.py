# -*- coding: utf-8 -*-

from .metodos_basicos import *

def euler(edo, valor_inicial, valor_final, condicao_inicial, numero_passos):

	h = (valor_final-valor_inicial)/float(numero_passos)
	
	t = valor_inicial
	x0 = condicao_inicial	
	x = [x0]

	for i in range(numero_passos):

		x0 += h * edo(t,x0)
		t += h

		x.append(x0)

	return x

def runge_kutta_ordem2(edo, valor_inicial, valor_final, condicao_inicial, numero_passos):

	h = (valor_final-valor_inicial)/float(numero_passos)
	
	t = valor_inicial
	x0 = condicao_inicial	
	x = [x0]

	for i in range(numero_passos):

		x0 += (h/2) * (edo(t,x0) + edo(t+h, x0 + h*edo(t,x0)))
		t += h

		x.append(x0)

	return x	

def runge_kutta_ordem4(edo, valor_inicial, valor_final, condicao_inicial, numero_passos):

	h = (valor_final-valor_inicial)/float(numero_passos)
	
	t = valor_inicial
	x0 = condicao_inicial	
	x = [x0]

	for i in range(numero_passos):

		K1 = edo(t, x0) 
		K2 = edo(t+(h/2), x0 + (h/2)*K1)
		K3 = edo(t+(h/2), x0 + (h/2)*K2)
		K4 = edo(t+h, x0 + h*K3)

		x0 += (h/6) * (K1 + 2*K2 + 2*K3 +K4)
		t += h

		x.append(x0)

	return x