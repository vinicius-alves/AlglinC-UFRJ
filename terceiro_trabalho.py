# -*- coding: utf-8 -*-

import my_lib  

array_X_valores = [1,2,3]
array_Y_valores = [1,2,9]

array_X = my_lib.criar_array(array_X_valores)
array_Y = my_lib.criar_array(array_Y_valores)

#Exercício 1

matriz_B = my_lib.interpolacao_polinomial(array_X,array_Y)

print"Exercício 1"

my_lib.print_polinomio(matriz_B)

#Exercício 2

array_X_valores = [1,2,3, 4]
array_Y_valores = [1,2,9,20]

array_X = my_lib.criar_array(array_X_valores)
array_Y = my_lib.criar_array(array_Y_valores)

matriz_B = my_lib.interpolacao_polinomial(array_X,array_Y)

print"Exercício 2"

my_lib.print_polinomio(matriz_B)

print"Exercício 4"

my_lib.interpolacao_lagrange(array_X,array_Y)

