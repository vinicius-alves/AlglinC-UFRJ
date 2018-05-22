# -*- coding: utf-8 -*-

import my_lib
import numpy as np

# Exercício 1

function_I1 = lambda t,y: -2*t*y**2
y0 = 1.0
valor_inicial = 0.0
valor_final = 2.0
numero_passos = 30

print my_lib.euler(function_I1,valor_inicial,valor_final,y0,numero_passos)
print ""
print my_lib.runge_kutta_ordem2(function_I1,valor_inicial,valor_final,y0,numero_passos)
print ""
print my_lib.runge_kutta_ordem4(function_I1,valor_inicial,valor_final,y0,numero_passos)