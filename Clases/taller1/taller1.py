#Taller 1
#1.utilizano python determinar el perdiodo de las siguientes señales
#a) 4sin(7t) +25cos(15t)
#b) (6sen(3t)+4sen(7t))al 2
#2determinar si son funciones pares, impares o ningunas
#
#
#

import sympy as sym


sym.init_printing()


def a():

    t = sym.symbols('t')
    xt =  4 * sym.sin(7*t)+ 25* sym.cos(15*t)
    #sym.plot(xt)
    sym.pprint(xt)
def b():

    t = sym.symbols('t')
    xt =  (6* sym.sin(3*t) + 4* sym.sin(7 *t))**2
    #sym.plot(xt,xlim = [-5,5])

a()
