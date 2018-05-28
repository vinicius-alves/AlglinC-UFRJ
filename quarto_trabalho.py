# -*- coding: utf-8 -*-

import my_lib
import numpy as np
from inspect import getsource

print '\nMétodo da Bisseção:\n' 

# Aplicação 1

g = 9.806
k = 0.00341

function_1 = lambda x : np.log(np.cosh(x*np.sqrt(g*k))) - 50

print getsource(function_1)

xzero = np.zeros(2)

xzero[0] = my_lib.bissecao(function = function_1, a = -300 , b = 0 )
xzero[1] = my_lib.bissecao(function = function_1, a = 0  , b = 300 )

for i in range(len(xzero)):
	print "xzero["+str(i)+"] = "+str(xzero[i])

#my_lib.visualizar_funcao(function = function_1, xmin = -600, xmax = 600, xzero = xzero)

print '\n'

# Aplicação 2

function_2 = lambda x : 4*np.cos(x) - np.exp(2*x)

print getsource(function_2)

xzero = np.zeros(1)

xzero[0] = my_lib.bissecao(function = function_2, a = -20  , b = 4 )

for i in range(len(xzero)):
	print "xzero["+str(i)+"] = "+str(xzero[i])

#my_lib.visualizar_funcao(function = function_2, xmin = -20, xmax = 4, xzero = xzero)

print '\n'

# função precisa ser f(x) = 0 e o número de variáveis sempre deve ser igual  
functions = [lambda x1,x2: x1+2*x2-2,
			 lambda x1,x2: np.power(x1,2) + 4*np.power(x2,2) -4  
			]

my_lib.metodo_newton_sistemas_nl(functions = functions, num_variaveis = 2)
