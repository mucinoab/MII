"""
This file is where all the methods where tested and/or prototyped

"""

import time
import matplotlib.pyplot as plt
import numpy as np
import sympy
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def estiliza_string(fucn):
    superscript_map = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸",
                       "9": "⁹", "x": "ˣ", "y": "ʸ", "z": "ᶻ"}
    nuevo = ''
    c = 0
    p = len(fucn)
    #
    while c < p:
        if fucn[c] == '*':
            if fucn[c + 1] == '*':
                nuevo += superscript_map[fucn[c + 2]]
                c += 2
        else:
            nuevo += fucn[c]
        c += 1
    return nuevo

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
print(x)
{

print("Newton multivariable")

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
print(x)
print((' '.join(map(str, j))))

# -----------------------------------------------------------------------------------------

import sympy
from sympy import *
import time

# Calculando valores

iteraciones = 10000
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
start = time.time()

fxn = sympy.lambdify([x,y], fux, "numpy")
fyn = sympy.lambdify([x,y], fuy, "numpy")

fxxn = sympy.lambdify([x,y], fx, "numpy")
fyyn = sympy.lambdify([x,y], fy, "numpy")


for q in range(1, iteraciones + 1):

    x0 = fxxn(x0, y0)
    y0 = fyyn(x0, y0)

    num = fxn(x0, y0)
    num2 = fyn(x0, y0)

    print(q, x0, y0, num, num2)
    resul['filas'].append([q, x0, y0, num, num2])

end = time.time()
print(end - start)

# -----------------------------------------
print("Polinomio de Lagrange")
#         x|f(x)
#        -------
#         0|1
#
start = time.time()
datos = [(1, 56.5),
         (5, 113),
         (20, 181),
         (40, 214.5)]
grado = 0

x = sympy.symbols('x')


def poli_lag(grado, datos):
    x = sympy.symbols('x')
    resul = ""

    for i in range(0, grado + 1):
        resul += f"{datos[i][1]}"
        for j in range(0, grado + 1):
            if j != i:
                resul += f"*((x-{datos[j][0]})/({datos[i][0]}-{datos[j][0]}))"

        resul += '+'
    resul = resul.strip("+")
    print(resul)
    return sympy.lambdify(x, resul, "math"), sympy.sympify(resul)


f, fx = poli_lag(len(datos) - 1, datos)
t = np.arange(datos[0][0] - 2, datos[-1][0] + 2, (datos[1][0] - datos[0][0]) / 5)
s = []
m = []
gx = "x**3"
g = sympy.lambdify(x, gx, "math")
for n in t:
    s.append(f(n))
    m.append(g(n))

fig, ax = plt.subplots()
plt.rc_context({"axes.titlesize": "large", 'legend.fontsize': 'large'})

ax.plot(t, s, color='#40E0D0')
ax.plot(t, s, label=f'Polinomio de Lagrange = {estiliza_string(str(sympy.simplify(fx)))}', color='#40E0D0')
ax.plot(t, m, label=f'Función Original = {estiliza_string(gx)}', color='green')

for n in range(len(datos) - 1):
    plt.plot(datos[n][0], datos[n][1], marker='o', markersize=5, color="red")

plt.plot(datos[-1][0], datos[-1][1], marker='o', markersize=5, color="red", label=f"Puntos dados")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(color="gray")
plt.legend(loc='best')
plt.tight_layout()

print("latex: ", str(sympy.latex(fx)))
print("Simplificando: ", estiliza_string(str(sympy.simplify(fx))))
print(f"{f(10)}")
print("Todo en " + str(time.time() - start) + " segundos.")
plt.show()


# -----------------------------------------
p_n, empezando desde 0
P_n(x) = c0 + c1(x-x0) + c2(x-x0)(x-x1) + ... + cn(x-x0)(x-x1)...(x-xn-1)
print("Diferencias Divididas\n\n")
       x | f(x_i)
datos = [(1, Fraction('2/3')),
         (3, 1),
         (5, -1),
         (6, 0)]

print(datos, "---")

res = ""

for x in range(0, len(datos)):
    res += f"c{x}"

    for y in range(0, x):
        res += f"(x-x{y})"

    res += "+"

res = res.strip("+")
print(res)

res = ""
cs = ""

for x in range(0, len(datos)):
    res += f"c_{x}"
    cs += f" c_{x}"

    for y in range(0, x):
        res += f"*(x-{datos[y][0]})"

    res += "+"

res = ""

for x in range(0, len(datos)):
    res += f"c_{x}"
    cs += f" c_{x}"

    for y in range(0, x):
        res += f"(x-{datos[y][0]})"

    res += "+"

res = res.strip("+")

primeras = []
segundas = []
terceras = []

for x in range(len(datos) - 1):
    primeras.append(Fraction((datos[x + 1][1] - datos[x][1]) / (datos[x + 1][0] - datos[x][0])))

print(primeras)

for x in range(len(datos) - 2):
    segundas.append(Fraction((primeras[x + 1] - primeras[x]) / (datos[x + 2][0] - datos[x][0])))

print(segundas)

for x in range(len(datos) - 3):
    terceras.append(Fraction((segundas[x + 1] - segundas[x]) / (datos[x + 3][0] - datos[x][0])))

print(terceras)

print("\n\nCoeficientes newton diferencias divididas hacia adelante\n", datos[0][1], primeras[0], segundas[0],
      terceras[0])

poliD = res.replace("c_0", str(datos[0][1])).replace("c_1", str(primeras[0])).replace("c_2", str(segundas[0])).replace(
    "c_3", str(terceras[0]))

res = ""

for x in range(0, len(datos)):
    res += f"c_{x}"

    for y in range(0, x):
        print(y)
        res += f"(x-{datos[abs(y - len(datos) + 1)][0]})"

    res += "+"

res = res.strip("+")
poliA = res.replace("c_0", str(datos[-1][1])).replace("c_1", str(primeras[-1])).replace("c_2",
                                                                                        str(segundas[-1])).replace(
    "c_3", str(terceras[-1]))

print(res)
print()
print(poliD)
print()
print(poliA)

# ----------------------------------------------------------------------------
import sympy
import numpy as np
print("Regla Tra")
funcion = input("Ingresa la función a Integrar:  ")
I1 = float(input("Primer Intervalo:  "))
I2 = float(input("Segundo Intervalo: "))

x, y, z, w, t = sympy.symbols('x y z w t')
fsym = sympy.sympify(funcion)
fx = sympy.lambdify(x, fsym, "math")


h = .01
rango = (int(I2 - I1) + 1)/h
x_i = np.arange(I1, I2 + 1, h)
c_i = np.ones(rango)
fx_i = []
c_i[0] = .5
c_i[-1] = .5

sum = []
sigma = 0

for n in x_i:
    fx_i.append(fx(n))

for n in range(0, rango):
    sum.append(c_i[n] * fx_i[n])

print()
print(fx_i, len(fx_i))
print(c_i, len(c_i))
print(sum, len(sum))
print(f"\[\int_{I1}^{I2} \> {funcion} \> dx =   \]")

for n in sum:
    sigma += n

def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    print(f"h = {h}")
    s = 0.0
    s += f(a)/2.0
    print(f"{(a):.4f} || {f(a*h)} || {h} || {(h*f(a*h)):.4f}")
    for i in range(1, n):
        print(f"{(a+h*i):.4f} || {f(a+i*h)} || {h} || {(h*f(a+i*h)):.4f}")
        s += f(a + i*h)
    s += f(b)/2.0
    print(f"{(a+h*i):.4f} || {f(a+i*h)} || {h} || {(h*f(a+i*h)):.4f}")
    return s * h

print( trapezoidal(fx, 0, .4, 10))
print("Valor real: ", sympy.integrate(fsym, (x, I1, I2)))

# --------- graficacion ------------

t = np.linspace(I1 - (I2 // I1), I2 + (I2 // I1))
s = []

for n in t:
    s.append(fx(n))

plt.rc_context({'axes.edgecolor': 'black', 'xtick.color': 'black', 'ytick.color': 'black'})
fig, ax = plt.subplots()

ax.plot(t, s, label=f'f(x) = {funcion}', color='#40E0D0')
# ax.grid(color="gray")
ax.set_ylim(bottom=0)

ix = np.linspace(I1, I2)
iy = fx(ix)
verts = [(I1, 0), *zip(ix, iy), (I2, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
ax.text(0.5 * (I1 + I2), 30, f"$\int_{{I1}}^{{I2}} {sympy.latex(fsym)}\>dx$",
        horizontalalignment='center', fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((I1, I2))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([])

plt.show()

# --------------------------------------------------------------------------------------------

from operator import itemgetter

import time
from sympy import init_printing,
import matplotlib.pyplot as plt
import numpy as np
import sympy

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

sympy.init_printing()

funcion = input("Función a integrar: ")
I1 = float(input("Primer intervalo: "))
I2 = float(input("Segundo intervalo: "))

x = sympy.symbols('x')
f = sympy.sympify(funcion)
fx = sympy.lambdify(x, f, "math")

fnueva = funcion.replace('x', str(I1))
deltax = (I2 - I1) / 10

i = 0
p = 1
 
while i <= I2:
    if (p%2) != 0:
        fnueva += f" + 4*({funcion.replace('x', str(i))})*x"
    else:
        fnueva += f" + 2*{funcion.replace('x', str(i))}*x"

    i += deltax
    p += 1


fnueva += "+"+funcion.replace('x', str(I2))
fnueva = f"{deltax}/3*("+ fnueva + ")"
#print(fnueva)
g = sympy.sympify(fnueva)
gx = sympy.lambdify(x, g)


curi = f"((({I2-I1})/2)/3)*({funcion.replace('x', str(I1))}+4*({funcion.replace('x', str((I1+I2)/2))}+{funcion.replace('x', str(I2))})) "
print(f"valor real: {sympy.integrate(f, (x, I1, I2))}")  # , f"valor calculado: {gx(1)}", curi, sympy.sympify(curi))


def simpson(f, a, b, n):
    tabla = []
    k = 0.0
    h = (b - a) / n
    print(h, n)
    x = a + h

    aux = f(a)

    tabla.append([1, aux, 1, aux])

    for i in range(1, int(n / 2) + 1):
        aux = f(x)
        tabla.append([x, aux, 4, aux * 4])
        k += 4 * aux
        x += 2 * h

    x = a + 2 * h

    for i in range(1, int(n / 2)):
        aux = f(x)
        tabla.append([x, aux, 2, aux * 2])
        k += 2 * aux
        x += 2 * h

    aux = f(b)
    tabla.append([b, aux, 1, aux])

    tabla.sort(key=itemgetter(0))

    for n in tabla:
        print(f"{n[0]:.3f} &{n[1]:.3f} &{n[2]:.3f} &{n[3]:.3f} \\\\\n\hline")
        

    return (h / 3) * (f(a) + aux + k)


print(f"valor real: {sympy.integrate(f, (x, I1, I2))}")  # , f"valor calculado: {gx(1)}", curi, sympy.sympify(curi))
print(f"valor colculado: {simpson(fx, (I1), (I2), 10)}")


print("Simpson 3/8")


funcion = input("Función a integrar: ")
a = float(input("Primer intervalo: "))
b = float(input("Segundo intervalo: "))
n = float(input("saltos: "))

x = sympy.symbols('x')
f = sympy.sympify(funcion)
fx = sympy.lambdify(x, f, "math")

print(f"valor real: {sympy.integrate(f, (x, I1, I2))}")
def calculate(f, a, b, n):
    sum = 0
    h = (float(b - a) / n)
    aux = f(a)
    sum = aux + f(b);

    print(a, aux, 1, aux)

    for i in range(1, n):
        aux = f(a + i * h)
        if (i % 3) == 0:
            print(a+i*h, aux, 2, 2*aux)
            sum = sum + 2 * (aux)

        else:
            print(a+i*h, aux, 3, 3*aux)
            sum = sum + 3 * (aux)

    aux = f(b)
    print(b, aux, 1, aux)

    return ((float(3 * h) / 8) * sum)


integral_res = calculate(fx, a, b, n)

print(integral_res)
