import numpy as np
import my_lib  

matriz_linhas = [
	[5,1,0],
	[3,2,7],
	[2,0,1]
]

matriz = my_lib.criar_matriz(matriz_linhas)

matriz_L, matriz_U = my_lib.decomposicaoLU(matriz)