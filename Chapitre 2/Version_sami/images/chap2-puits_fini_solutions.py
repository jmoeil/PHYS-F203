from sympy import *

x = Symbol('x', real=True)

eq = Eq(x/5 - cos(x))

solve([eq], x)

