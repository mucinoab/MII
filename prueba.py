from sympy import symbols, series, sympify, solve, latex, init_printing
from sympy.core import S
#https://docs.sympy.org/latest/modules/solvers/solvers.html

#x*y**2+x-10*y+8
#x**2-10*x+y**2+8

print("Punto fijo")

x, y, z = symbols('x y z')
# init_printing()

fux = sympify("x**2-10*x+y**2+8")
fuy = sympify("x*y**2+x-10*y+8")

# print(series(fux, x, 0, 1), "hola")

fx = sympify(str(solve(fux, x, implicit=True, manual=True, rational=True)).strip('[]'))
fy = sympify(str(solve(fuy, y, implicit=True, manual= True, rational=True)).strip('[]'))

print(fux, "----", fx)
nx = 0
ny = 0

for z in range(10):
    # nx = (fx.subs({x: nx, y: ny}))
    # ny = (fy.subs({x: nx, y: ny}))

    nx = round(fx.subs({x: nx, y: ny}), 20)
    ny = round(fy.subs({x: nx, y: ny}), 20)

    print(nx.n(8), ny.n(8))#, fx.subs({ x: nx, y: ny}), fy.subs({ x: nx, y: ny}), '\n')

print(fx.subs({ x: nx, y: ny}).n(8), fy.subs({ x: nx, y: ny}).n(8), abs(fx.subs({ x: nx, y: ny}).n(20)-fy.subs({ x: nx, y: ny}).n(20)), '\n')


# print(latex(S('x*y**2+x-10*y+8',evaluate=False) ,mode='equation'))

# to do:
#     la cosa de derivacion para acotar intervalos
#
#
#
#



















