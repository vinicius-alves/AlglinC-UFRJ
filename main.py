import numpy as np
import my_lib  

matriz_A_linhas = [
	[ 5,-4, 1, 0],
	[-4, 6,-4, 1],
	[ 1,-4, 6,-4],
	[ 0, 1,-4, 5]
]

matriz_B_linhas = [
	[-1],
	[ 0],
	[ 1],
	[ 0]
]

matriz_A = my_lib.criar_matriz(matriz_A_linhas)

matriz_B = my_lib.criar_array(matriz_B_linhas)

matriz_L, matriz_U = my_lib.decomposicaoLU(matriz_A)

matriz_Y = my_lib.multiplicacao_retro_substituicao(matriz_L,matriz_B)

matriz_X =  my_lib.multiplicacao_substituicao_para_frente(matriz_U, matriz_Y)

print(matriz_X)
