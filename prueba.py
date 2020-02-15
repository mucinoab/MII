from sympy import symbols, sympify, solve, latex, init_printing
from sympy.core import S
#https://docs.sympy.org/latest/modules/solvers/solvers.html

#x*y**2+x-10*y+8
#x**2-10*x+y**2+8

print("Punto fijo")

x, y, z, t = symbols('x y z t')
init_printing()

fux = sympify("x**2-10*x+y**2+8")
fuy = sympify("x*y**2+x-10*y+8")

fx = sympify(str(solve(fux, x, implicit=True, quick=True, manual=True)).strip('[]'))
fy = sympify(str(solve(fuy, y, implicit=True, quick=True, manual= True)).strip('[]'))

nx = 3
ny = 3

for z in range(100):
    # nx = (fx.subs({x: nx, y: ny}))
    # ny = (fy.subs({x: nx, y: ny}))

    nx = round(fx.subs({x: nx, y: ny}))
    ny = round(fy.subs({x: nx, y: ny}))

    print(nx.n(8), ny.n(8))#, fx.subs({ x: nx, y: ny}), fy.subs({ x: nx, y: ny}), '\n')

print(nx.n(8), ny.n(8), fx.subs({ x: nx, y: ny}).n(8), fy.subs({ x: nx, y: ny}).n(8), '\n')


print(latex(S('x*y**2+x-10*y+8',evaluate=False) ,mode='equation'))

# to do:
#     la cosa de derivacion para acotar intervalos
#
#
#
#



















