import sympy as sym


T = 2
w0 = sym.pi
t = sym.symbols('t', real = True)
n = sym.symbols('n')
#n =  sym.symbols = ('n')
print ('ao=')
#declaramos la integral
a0 = (sym.integrate(t+1,(t,-1,0)) + sym.integrate(-t+1 , (t,0,1)))/T

sym.pprint(a0)

print ('an=')
an = 2 * (sym.integrate((t+1)*sym.cos(n * w0 * t), (t,-1,0))+ sym.integrate((-t +1)*sym.cos(n *w0*t),(t,0,1)))/T
sym.pprint(an)

print ('bn=')
bn=2*(sym.integrate((t+1)*sym.sin(n*w0*t), (t, -1, 0)) + sym.integrate((-t+1)*sym.sin(n*w0*t), (t, 0, 1)))/T
sym.pprint(bn)


#a mano
#Ft = a0 +(4/(sym.pi**2))* sym.cos(w0 * t) + (2/(9 *sym.pi **2))* 2 * sym.cos(3 * w0 *t) + (2/( 25 * sym.pi **2))*2* sym.cos(5 * w0 *t) + (2/( 49 * sym.pi **2))*2* sym.cos(7 * w0 *t)

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

#DrawFourier(a0,an,bn,w0,t,n,500)
DrawFourierDeriv(a0,an,bn,w0,t,n,7)
#print(Ft)
#sym.plot(Ft)
