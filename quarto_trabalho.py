# -*- coding: utf-8 -*-

import my_lib
import numpy as np
from inspect import getsource

def imprimir_vetor_xzero(vetor_xzero):
	for i in range(len(xzero)):
		print "   xzero["+str(i)+"] = "+str("%.4f"%xzero[i])

print '\nAplicacao 1:\n' 

g = 9.806
k = 0.00341

function_1 = lambda x : np.log(np.cosh(x*np.sqrt(g*k))) - 50

print getsource(function_1)

xzero = np.zeros(2)

print '\n   Bissecao:\n' 

xzero[0] = my_lib.bissecao(function = function_1, a = -300 , b = 0 )
xzero[1] = my_lib.bissecao(function = function_1, a = 0  , b = 300 )

imprimir_vetor_xzero(xzero)

print '\n   Newton original:\n' 

xzero[0] = my_lib.metodo_newton_original(function = function_1, ponto_inicial = -10)
xzero[1] = my_lib.metodo_newton_original(function = function_1, ponto_inicial =  10)

imprimir_vetor_xzero(xzero)

print '\n   Newton secante:\n' 

xzero[0] = my_lib.metodo_newton_secante(function = function_1, ponto_inicial = -10)
xzero[1] = my_lib.metodo_newton_secante(function = function_1, ponto_inicial =  10)

imprimir_vetor_xzero(xzero)

#my_lib.visualizar_funcao(function = function_1, xmin = -600, xmax = 600, xzero = xzero)

print '\n'

print '\nAplicacao 2:\n' 

function_2 = lambda x : 4*np.cos(x) - np.exp(2*x)

print getsource(function_2)

xzero = np.zeros(1)

print '\n   Bissecao:\n' 

xzero[0] = my_lib.bissecao(function = function_2, a = -20  , b = 4 )

imprimir_vetor_xzero(xzero)

print '\n   Newton original:\n' 

xzero[0] = my_lib.metodo_newton_original(function = function_2, ponto_inicial = -10)

imprimir_vetor_xzero(xzero)

print '\n   Newton secante:\n' 

xzero[0] = my_lib.metodo_newton_original(function = function_2, ponto_inicial = -10)

imprimir_vetor_xzero(xzero)

#my_lib.visualizar_funcao(function = function_2, xmin = -20, xmax = 4, xzero = xzero)


print '\nResolucao de sistemas nao lineares:' 

print "Sistema: \n"

# função precisa ser f(x) = 0 e o número de variáveis sempre deve ser igual  
functions = [
lambda x1,x2: x1+2*x2-2,
lambda x1,x2: np.power(x1,2) + 4*np.power(x2,2) -4  
			]

for function in functions:
	print getsource(function)

print '\n Metodo de Newton' 

vetor_solucao = my_lib.metodo_newton_sistemas_nl(functions = functions, num_variaveis = 2, vetor_x = [2,3])

for i in range(len(vetor_solucao)):
	print "vetor_solucao["+str(i)+"] = "+str("%.3f" % vetor_solucao[i])


print '\n Metodo de Broyden' 

vetor_solucao = my_lib.metodo_broyden_sistemas_nl(functions = functions, num_variaveis = 2, vetor_x = [2,3])

for i in range(len(vetor_solucao)):
	print "vetor_solucao["+str(i)+"] = "+str("%.3f" % vetor_solucao[i])

