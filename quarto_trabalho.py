# -*- coding: utf-8 -*-

import my_lib  

function = lambda x : x + 2

#x_zero = my_lib.bissecao(function = function, search_a_b = True)
x_zero = my_lib.bissecao(function = function, a = -10 , b = 10 )

print "\nx_zero = "+str(x_zero)+"\n"

# Aplicação 1