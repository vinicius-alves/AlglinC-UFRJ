# -*- coding: utf-8 -*-

import my_lib 

#Parte 1

A = [[4.5,2.5,1.5,0.5,1.0,0.5],
	 [2.5,5.0,2.5,1.5,0.5,1.0],
	 [1.5,2.5,4.5,2.5,0.5,1.0],
	 [0.5,1.5,2.5,3.0,0.5,1.0],
	 [1.0,0.5,0.5,0.5,2.5,1.5],
	 [0.5,1.0,1.0,1.0,1.5,2.0]]

B = [[ 30],
	 [ 10],
	 [ 10],
	 [-10],
	 [ 0],
	 [ 5]]

A_matriz = my_lib.criar_matriz(A)
B_matriz = my_lib.criar_matriz(B)

print my_lib.decomposicaoCholesky(A_matriz)
A_Cholesky = my_lib.decomposicaoCholesky(A_matriz)

print my_lib.decomposicaoLU(A_matriz)
A_LU = my_lib.decomposicaoLU(A_matriz)

print my_lib.jacobiMethod(A_matriz)

print my_lib.resolver_sistema_por_decomposicao_LU(A_matriz,B_matriz)

print my_lib.resolver_sistema_por_decomposicao_de_Cholesky(A_matriz,B_matriz)

print my_lib.det(A)

print my_lib.detCholesky(A_Cholesky)

print my_lib.detLU(A_LU)

#Parte 2

X = [[-2.7,2.25],
	 [-1.0,3.45],
	 [ 0.0,4.5],
	 [ 1.0,5.625],
	 [ 1.6,6.375],
	 [ 3.1,7.125]]

print my_lib.regressaoLinear(X)