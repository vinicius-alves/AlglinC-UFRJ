# -*- coding: utf-8 -*-

import my_lib
import numpy as np
import scipy.integrate as integrate
import scipy.special as special

# Exercício 2

function_I1 = lambda x: (1/np.sqrt(2*np.pi))*np.exp(-0.5*x**2), 0.0, 1.0
function_I2 = lambda x: (1/np.sqrt(2*np.pi))*np.exp(-0.5*x**2), 0.0, 5.0

print my_lib.quadratura_Gauss(function_I1)
print my_lib.quadratura_Gauss(function_I2)
print ""
#print integrate.quad(lambda x: (1/np.sqrt(2*np.pi))*np.exp(-0.5*x**2), 0.0, 1.0)
#print integrate.quad(lambda x: (1/np.sqrt(2*np.pi))*np.exp(-0.5*x**2), 0.0, 5.0)
#print ""

#Exercício 3 (Para integração polinomial, número de pontos máximo = 13)

function_S = lambda x: (1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*2, 0.0, 10.0
function_S2 = lambda x: x**2*(1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*2, 0.0, 10.0

print my_lib.integracao_polinomial(function_S)
print my_lib.quadratura_Gauss(function_S2)
print ""

#print integrate.quad(lambda x: (1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*2, 0, 10.0)
#print integrate.quad(lambda x: x**2*(1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*2, 0, 10.0)
#print ""

#Exercício 4 (Para integração polinomial, número de pontos máximo = 13)

function_X = lambda x: (1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*(((4*np.pi**3*9.0)/(x**5*5.0**4+0.00000000000000001))*np.exp((-16*np.pi**3)/(x**4*5.0**4+0.00000000000000001))), 0.0, 10.0
function_X2 = lambda x: x**2*(1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*(((4*np.pi**3*9.0)/(x**5*5.0**4+0.00000000000000001))*np.exp((-16*np.pi**3)/(x**4*5.0**4+0.00000000000000001))), 0.0, 10.0

print my_lib.quadratura_Gauss(function_X)
print my_lib.integracao_polinomial(function_X2)
print ""

#print integrate.quad(lambda x: (1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*(((4*np.pi**3*9.0)/(x**5*5.0**4))*np.exp((-16*np.pi**3)/(x**4*5.0**4))), 0.0, 10.0)
#print integrate.quad(lambda x: x**2*(1/(np.sqrt((1-(x/1.0)**2)**2+(2*0.05*(x/1.0))**2)))**2*(((4*np.pi**3*9.0)/(x**5*5.0**4))*np.exp((-16*np.pi**3)/(x**4*5.0**4))), 0.0, 10.0)
#print ""

#Exercício 5 (N = 3 para integração polinomial; N = 2 para quadratura de Gauss)

function_5 = lambda x: 2+2*x-x**2+3*x**3, 0.0, 4.0

print my_lib.integracao_polinomial(function_5)
print my_lib.quadratura_Gauss(function_5)
print ""	
#print integrate.quad(lambda x: 2+2*x-x**2+3*x**3, 0.0, 4.0)
#print ""

#Exercício 6 (Ponto Médio: N = 1; Trapézio: N = 2; Simpson: N = 3)

function_6 = lambda x: 1.0/(1.0+x**2), 0.0, 3.0

print my_lib.quadratura_Gauss(function_6)
print my_lib.integracao_polinomial(function_6)
print my_lib.quadratura_Gauss(function_6)
#print ""
#print integrate.quad(lambda x: 1.0/(1.0+x**2), 0.0, 3.0)