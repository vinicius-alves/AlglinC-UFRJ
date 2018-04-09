import my_lib  
import numpy as np

matriz_A_linhas = [
	[-5,-4,1,0],
	[-4,6,-4,1],
	[1,-4,6,-4],
	[0,1,-4,5]
]

matriz_B_linhas = [
	[-1],
	[0],
	[1],
	[0]
]

matriz_A = my_lib.criar_matriz(matriz_A_linhas)

matriz_B = my_lib.criar_array(matriz_B_linhas)

matriz_X = my_lib.resolver_sistema_por_decomposicao_LU(matriz_A, matriz_B)

#my_lib.print_array_resposta(matriz_X)


A = my_lib.criar_array(matriz_A_linhas)
B = my_lib.criar_array(matriz_B_linhas)

print(np.linalg.solve(A,B))

'''
M1_L = [
	[1,0,0,0],
	[-4/5,1,0,0],
	[1/5,0,1,0],
	[0,0,0,1]
]

M2_L = [
	[1,0,0,0],
	[0,1,0,0],
	[0,12/23,1,0],
	[0,-5/46,0,1]
]

M3_L = [
	[1,0,0,0],
	[0,1,0,0],
	[0,0,1,0],
	[0,0,16/17,1]
]


M1 = my_lib.criar_matriz(M1_L)

M2 = my_lib.criar_matriz(M2_L)

M3 = my_lib.criar_matriz(M3_L)

B = my_lib.criar_matriz(matriz_B_linhas)

print(M3*M2*M1*B)
'''