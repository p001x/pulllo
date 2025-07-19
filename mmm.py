import sympy as sym
x=sym.symbols('x')
func=sym.sin(x)**2+sym.exp(x**2)
derivaative=sym.diff(func,x)
print(derivative)