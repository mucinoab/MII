from sympy import symbols, sympify, solve, latex, init_printing
from sympy.core import S
#https://docs.sympy.org/latest/modules/solvers/solvers.html

#x**2-10*x+y**2+8
#x+y**2+x-10*y+8

print("Punto fijo")

x, y, z, t = symbols('x y z t')
init_printing()

fux = sympify("x**2-10*x+y**2+8")
fuy = sympify("x*y**2+x-10*y+8")

fx = sympify(str(solve(fux, x, implicit=True, quick=True, manual=True)).strip('[]'))
fy = sympify(str(solve(fuy, y, implicit=True, quick=True, manual= True)).strip('[]'))

nx = 5
ny = 3

for z in range(5):
    nx = round(fx.subs({x: nx, y: ny}))
    ny = round(fy.subs({x: nx, y: ny}))

    print(nx.n(8), ny.n(8), fx.subs({ x: nx, y: ny}).n(8), fy.subs({ x: nx, y: ny}).n(8), '\n')


print(latex(S('x*y**2+x-10*y+8',evaluate=False) ,mode='equation'))

# to do:
#     la cosa de derivacion para acotar intervalos
#
#
#
#



















