import time

import numpy as np
import sympy
from sympy import init_printing

init_printing()

print("Newton multivariable")
x, y = sympy.symbols('x y')

f1 = sympy.sympify("x**2-y**2-1")
f2 = sympy.sympify("x**2+y**2+x*y-4")

# derivadas parciales
f1x = sympy.diff(f1, x)
f1y = sympy.diff(f1, y)

f2x = sympy.diff(f2, x)
f2y = sympy.diff(f2, y)

# vector de las funciones iniciales
v = sympy.Matrix([[f1], [f2]])

j = sympy.Matrix([[f1x, f1y],
                  [f2x, f2y]])

j_inv = j ** -1  # inversa,de la jacobiana

jaco = sympy.lambdify([x, y], j_inv, 'numpy')
fxfy = sympy.lambdify([x, y], v, 'numpy')

x = np.ones((2, 1))

iteraciones = 1000

start = time.time()

for n in range(iteraciones):
    j = jaco(x[0][0], x[1][0]).dot(fxfy(x[0][0], x[1][0]))
    x = x - j
sol = fxfy(x[0][0], x[1][0])

print(sol)
print(f'{float(sol[0]):.6f}')

end = time.time()
# print(end - start)
# print(x)

# print((' '.join(map(str, j))))

# -----------------------------------------------------------------------------------------

# import sympy
# from sympy import *
# import time
#
# # Calculando valores
#
# iteraciones = 10000
# resul = {'titulos': ['n', 'Xn', 'Yn', 'f(x, y)', 'g(x, y)'], 'filas': []}
#
# x, y = sympy.symbols('x y')
#
# # Ejemplos de Curiel
# funx = "x**2-10*x+y**2+8"
# funy = "x*y**2+x-10*y+8"
#
# # despejes
# fx = "(x**2+y**2+8)/(10)"
# fy = "(x*y**2+x+8)/(10)"
#
# x0 = 0
# y0 = 0
#
# fux = sympy.sympify(funx)
# fuy = sympy.sympify(funy)
#
# fxx = sympy.sympify(fx)
# fyy = sympy.sympify(fy)
#
# #-------------------------------------------
# start = time.time()
#
# fxn = sympy.lambdify([x,y], fux, "numpy")
# fyn = sympy.lambdify([x,y], fuy, "numpy")
#
# fxxn = sympy.lambdify([x,y], fx, "numpy")
# fyyn = sympy.lambdify([x,y], fy, "numpy")
#
#
# for q in range(1, iteraciones + 1):
#
#     x0 = fxxn(x0, y0)
#     y0 = fyyn(x0, y0)
#
#     num = fxn(x0, y0)
#     num2 = fyn(x0, y0)
#
#     print(q, x0, y0, num, num2)
#     resul['filas'].append([q, x0, y0, num, num2])
#
# end = time.time()
# print(end - start)
