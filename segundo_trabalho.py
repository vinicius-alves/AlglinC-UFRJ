# -*- coding: utf-8 -*-

import my_lib  

#Exercício 4

matriz_A_linhas = [
	[ 3.0, 2.0, 0.0],
	[ 2.0, 3.0,-1.0],
	[ 0.0,-1.0, 3.0]
]

matriz_B_linhas = [
	[ 1.0],
	[-1.0],
	[ 1.0]
]

matriz_A = my_lib.criar_matriz(matriz_A_linhas)

matriz_B = my_lib.criar_array(matriz_B_linhas)

matriz_X = my_lib.powerMethod(matriz_A)

print matriz_X
print ""

matriz_X = my_lib.jacobiMethod(matriz_A)

print matriz_X