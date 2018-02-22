import sympy as sym

sym.init_printing()
t = sym.symbols('t', real = True)

A = 0.3
W1 = 3
B = .5
W2 = 5
'''
class rect(sym.Function):

    @classmethod
    def eval(cls, arg):

        return sym.Heaviside(arg + sym.S.Half) - sym.Heaviside(arg -sym.S.Half)'''

rect = sym.Heaviside(t + (1/2)) - sym.Heaviside(t -(1/2))
x = rect.subs(t, t - 1/2) + 2/3  * rect.subs(t,t - 3/2) + 1/3 * rect.subs(t,t -5/2)
x1 = 4/3*rect.subs(t, t - 1/2) + rect.subs(t,t - 3/2) + 2/3 * rect.subs(t,t -5/2)+1/3*rect.subs(t,t -7/2)

x3 = rect.subs(t,0.5* t - 1/2) + 2/3  * rect.subs(t,0.5*t - 3/2) + 1/3 * rect.subs(t,0.5*t -5/2)

y = x.subs(t, 2-t)
sym.plot(y, (t,-1,11), ylim = [-0.2 ,1.2], ylabel = r'$x(t)$')
