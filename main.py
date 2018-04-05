import numpy as np
import my_lib  

matriz_linhas = [
	[1,0,0],
	[0,1,0],
	[0,0,1]
]

matriz = my_lib.criar_matriz(matriz_linhas)

print(my_lib.transposta(matriz))