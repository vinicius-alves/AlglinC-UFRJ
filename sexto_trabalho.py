# -*- coding: utf-8 -*-

import my_lib
import numpy as np

# Exercício 1 (Falta comparar com (1/(1+t**2) - plotar gráfico de ambos)

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
print ""

# Exercício 2 (Euler Ordem 2 só converge com numero_passos grande (>5000); Runge-Kutta-Nystrom converge em numero_passos >200)
#			  (Falta plotar gráfico de ambos)

function_I2 = lambda t,y,dy: 2*np.sin(t*0.5) + np.sin(2*t*0.5) + np.cos(3*t*0.5) - y - 0.2*dy
y0 = 0.0
dy0 = 0.0
valor_inicial = 0.0
valor_final = 100.0
numero_passos = 200

print my_lib.euler_ordem2(function_I2,valor_inicial,valor_final,y0,dy0,numero_passos)
print ""
print my_lib.runge_kutta_nystrom(function_I2,valor_inicial,valor_final,y0,dy0,numero_passos)
print ""

# Exercício 3

function_I3 = lambda t,y,dy: -9.80665-dy*np.absolute(dy)
y0 = 0.0
dy0 = 0.0
valor_inicial = 0.0
valor_final = 1.0
numero_passos = 10

print my_lib.euler_ordem2(function_I3,valor_inicial,valor_final,y0,dy0,numero_passos)
print ""
print my_lib.runge_kutta_nystrom(function_I3,valor_inicial,valor_final,y0,dy0,numero_passos)
print ""