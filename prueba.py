# import sympy
# from sympy import init_printing, init_session, pprint
# init_printing()
#
# print("Newton multivariable")
# x, y = sympy.symbols('x y')
#
# f1 = sympy.sympify("x**2-y**2-1")
# f2 = sympy.sympify("x**2+y**2+x*y-4")
#
# f1x = sympy.diff(f1, x)
# f1y = sympy.diff(f1, y)
#
# f2x = sympy.diff(f2, x)
# f2y = sympy.diff(f2, y)
#
# v = sympy.Matrix([f1], [f2])
# sol = sympy.Matrix([[1], [1]])
#
# j = sympy.Matrix([[f1x, f1y],
#                   [f2x, f2y]])
#
# j_inv = j**-1 #inversa
#
# print("f1=", f1, "\nf2=", f2, '\n')
# pprint(j)
# print()
# pprint(j_inv)
#

# import matplotlib.pyplot as plt
# import numpy as np

#-----------------------------------------------------------------------------------------

import sympy
from sympy import *
import time

# Calculando valores

iteraciones = 1000
resul = {'titulos': ['n', 'Xn', 'Yn', 'f(x, y)', 'g(x, y)'], 'filas': []}

x, y = sympy.symbols('x y')

# Ejemplos de Curiel
funx = "x**2-10*x+y**2+8"
funy = "x*y**2+x-10*y+8"

# despejes
fx = "(x**2+y**2+8)/(10)"
fy = "(x*y**2+x+8)/(10)"

x0 = 0
y0 = 0

fux = sympy.sympify(funx)
fuy = sympy.sympify(funy)

fxx = sympy.sympify(fx)
fyy = sympy.sympify(fy)

#-------------------------------------------

fxn = sympy.lambdify([x,y], fux, "numpy")
fyn = sympy.lambdify([x,y], fuy, "numpy")

fxxn = sympy.lambdify([x,y], fx, "numpy")
fyyn = sympy.lambdify([x,y], fy, "numpy")


start = time.time()
for q in range(1, iteraciones + 1):

    x0 = round(fxxn(x0, y0), 6)
    y0 = round(fyyn(x0, y0), 6)

    num = fxn(x0, y0)
    num2 = fyn(x0, y0)

    resul['filas'].append([q, x0, y0, num, num2])

end = time.time()
print(end - start)

