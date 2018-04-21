# -*- coding: utf-8 -*-

import my_lib  

print"Exercício 1"

array_X_valores = [1,2,3]
array_Y_valores = [1,2,9]

array_X = my_lib.criar_array(array_X_valores)
array_Y = my_lib.criar_array(array_Y_valores)

array_B = my_lib.interpolacao_polinomial(array_X,array_Y)
my_lib.print_polinomio(array_B)

funcao_exercicio_1 = array_B

print"Exercício 2"

array_X_valores = [1,2,3, 4]
array_Y_valores = [1,2,9,20]

array_X = my_lib.criar_array(array_X_valores)
array_Y = my_lib.criar_array(array_Y_valores)

array_B = my_lib.interpolacao_polinomial(array_X,array_Y)

my_lib.print_polinomio(array_B)

funcao_exercicio_2 = array_B

print"Exercício 4"

polinomioLagrange = my_lib.interpolacao_lagrange(array_X,array_Y)
my_lib.print_polinomio(polinomioLagrange)

funcao_exercicio_4 = polinomioLagrange

print "Exercício 6"

ponto_alvo = 3.5

print "Valor do ponto " + str(ponto_alvo) + " na função do primeiro exercício: " +str("%.3f" % my_lib.valor_polinomio_no_ponto(funcao_exercicio_1,ponto_alvo))
print "Valor do ponto " + str(ponto_alvo) + " na função do segundo  exercício: " +str("%.3f" % my_lib.valor_polinomio_no_ponto(funcao_exercicio_2,ponto_alvo))
#print "Valor do ponto " + str(ponto_alvo) + " na função do terceiro exercício: " +str(my_lib.valor_polinomio_no_ponto(funcao_exercicio_3,ponto_alvo))
print "Valor do ponto " + str(ponto_alvo) + " na função do quarto   exercício: " +str("%.3f" % my_lib.valor_polinomio_no_ponto(funcao_exercicio_4,ponto_alvo))
#print "Valor do ponto " + str(ponto_alvo) + " na função do quinto   exercício: " +str(my_lib.valor_polinomio_no_ponto(funcao_exercicio_5,ponto_alvo))

