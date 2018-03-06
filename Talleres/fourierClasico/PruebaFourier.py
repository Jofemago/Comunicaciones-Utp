import sympy as sym

#funcion es par
T = 2*sym.pi
w0 = 1
t = sym.symbols('t', real = True)
n = sym.symbols('n')
#n =  sym.symbols = ('n')
print ('ao=')
#declaramos la integral

F = sym.cos(t/2)
a0 = (1/T) * sym.integrate(F, (t,-1*sym.pi,sym.pi))

sym.pprint(a0)

print ('an=')
an = (2/T)*sym.integrate(F * sym.cos(n * w0 *t), (t,-1*sym.pi,sym.pi))
sym.pprint(an)

bn = 0



#usando el subs de sympy para reemplzar
def DrawFourier(a0,an,bn,wo,t,n, armonicos):
    Ft = an * sym.cos(n * w0 * t) + bn * sym.sin(n *w0* t)
    j = a0
    for i in range(1,armonicos):

        j += Ft.subs(n, i)

    sym.plot(j)

def DrawFourierDeriv(a0,an,bn,wo,t,n, armonicos):

    anp = bn * n *wo
    bnp = -1* an * n *wo
    fpt = anp* sym.cos(n * wo *t) + bnp * sym.sin( n *wo * t)
    j = 0
    for i in range(1, armonicos):

        j+= fpt.subs(n, i)

    sym.plot(j)

DrawFourier(a0,an,bn,w0,t,n,50 )
#DrawFourierDeriv(a0,an,bn,w0,t,n,7)
#print(Ft)
#sym.plot(Ft)
