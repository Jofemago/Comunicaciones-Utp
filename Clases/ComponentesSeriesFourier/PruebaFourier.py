import sympy as sym


T = 2
w0 = sym.pi
t, n = sym.symbols('t n', real = True)
#n =  sym.symbols = ('n')

#declaramos la integral
a0 = (sym.integrate(t+1,(t,-1,0)) + sym.integrate(-t+1 , (t,0,1)))/T

sym.pprint(a0)

an = 2 * (sym.integrate((t+1)*sym.cos(n * w0 * t), (t,-1,0))+ sym.integrate((-t +1)*sym.cos(n *w0*t),(t,0,1)))/T
sym.pprint(an)
