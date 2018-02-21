import sympy as sym

class Rect(sym.Function):

    @classmethod
    def eval(cls, arg):
        return  sym.Heaviside(arg + sym.S.Half) - sym.Heaviside(arg -sym.S.Half)


t =  sym.symbols('t', real= True)
x = Rect(t - 1/2) + 2/3 * Rect(t- 3/2) + 1/3 * Rect(t -5/2)
a = 1
y = x.subs(t, a*t)



y1 =  x.subs(t , (t-2)* -1)


sym.plot(y1, (t, -5,5), ylim = [-0.2,1.2], ylabel = r'$y(t)$')
