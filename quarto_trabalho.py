# -*- coding: utf-8 -*-

import my_lib
import numpy as np
from inspect import getsource
'''
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

'''
print '\nResolucao de sistemas nao lineares:' 

def imprimir_vetor_solucao(vetor_sol):
	for i in range(len(vetor_sol)):
		print "   vetor_solucao["+str(i)+"] = "+str("%.4f"%vetor_sol[i])


print '\nAplicacao 3:\n' 

print " Sistema: \n"

# função precisa ser f(x) = 0 e o número de variáveis sempre deve ser igual  
functions = [
  lambda x,y,z: 16*np.power(x,4) + 16*np.power(y,4) + np.power(z,4) -16,
  lambda x,y,z: np.power(x,2) + np.power(y,2) + np.power(z,2) -3,
  lambda x,y,z: np.power(x,3) - y + z -1
			]

for function in functions:
	print getsource(function)

print '\n Metodo de Newton\n' 

vetor_solucao = my_lib.metodo_newton_sistemas_nl(functions = functions, num_variaveis = 3, vetor_x = [1,1,1])

imprimir_vetor_solucao(vetor_solucao)

print '\n Metodo de Broyden\n' 

vetor_solucao = my_lib.metodo_broyden_sistemas_nl(functions = functions, num_variaveis = 3, vetor_x = [1,1,1])

imprimir_vetor_solucao(vetor_solucao)

print '\nAplicacao 4:\n' 

print " Sistema:"

teta_um   = 0
teta_dois = 0

# função precisa ser f(x) = 0 e o número de variáveis sempre deve ser igual  
functions = [
  lambda c2,c3,c4: 2*np.power(c3,2) + np.power(c2,2) + 6*np.power(c4,2) -1,
  lambda c2,c3,c4: 8*np.power(c3,3) + 6*c3*np.power(c2,2) + 36*c3*c2*c4 + 108*c3*np.power(c4,2) -teta_um,
  lambda c2,c3,c4: 60*np.power(c3,4) + 60*np.power(c3,2)*np.power(c2,2) + 576*c4*c2*np.power(c3,2) + 2232*np.power(c3,2)*np.power(c4,2) + 252*np.power(c4,2)*np.power(c2,2) + 1296*c2*np.power(c4,3) + 3348*np.power(c4,4) + 24*c4*np.power(c2,3) + 3*c2 - teta_dois
			]

valores_teta = [[0.0, 3.5],[0.75,6.5],[0.0,11.667]]

for valor_teta in valores_teta:

	teta_um   = valor_teta[0]
	teta_dois = valor_teta[1]

	print '\n'
	print 'teta_um:   ' + str(teta_um)
	print 'teta_dois: ' + str(teta_dois)


	print '\n Metodo de Newton\n' 

	vetor_solucao = my_lib.metodo_newton_sistemas_nl(functions = functions, num_variaveis = 3, vetor_x = [1,1,1])

	imprimir_vetor_solucao(vetor_solucao)

	print '\n Metodo de Broyden\n' 

	vetor_solucao = my_lib.metodo_broyden_sistemas_nl(functions = functions, num_variaveis = 3, vetor_x = [1,1,1])

	imprimir_vetor_solucao(vetor_solucao)