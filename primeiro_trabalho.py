import my_lib  

#Exercício 3

matriz_A_linhas = [
	[16,9,8,7,6,5,4,3,2,1],
	[9,17,9,8,7,6,5,4,3,2],
	[8,9,18,9,8,7,6,5,4,3],
	[7,8,9,19,9,8,7,6,5,4],
	[6,7,8,9,18,9,8,7,6,5],
	[5,6,7,8,9,17,9,8,7,6],
	[4,5,6,7,8,9,16,9,8,7],
	[3,4,5,6,7,8,9,15,9,8],
	[2,3,4,5,6,7,8,9,14,9],
	[1,2,3,4,5,6,7,8,9,13]
]

matriz_B_linhas = [
	[ 4],
	[ 0],
	[ 8],
	[ 0],
	[12],
	[ 0],
	[ 8],
	[ 0],
	[ 4],
	[ 0]
]

matriz_A = my_lib.criar_matriz(matriz_A_linhas)

matriz_B = my_lib.criar_array(matriz_B_linhas)

matriz_X = my_lib.resolver_sistema_por_decomposicao_LU(matriz_A, matriz_B)

my_lib.print_array_resposta(matriz_X)