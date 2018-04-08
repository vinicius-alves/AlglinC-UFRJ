import numpy as np
import my_lib  

matriz_A_linhas = [
	[1,2,2],
	[4,4,2],
	[4,6,4]
]

matriz_B_linhas = [
	[3],
	[6],
	[10]
]

matriz_A = my_lib.criar_matriz(matriz_A_linhas)

matriz_B = my_lib.criar_array(matriz_B_linhas)

matriz_X = my_lib.resolver_sistema_por_decomposicao_LU(matriz_A, matriz_B)

my_lib.print_array_resposta(matriz_X)

