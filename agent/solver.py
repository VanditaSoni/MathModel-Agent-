from sympy import symbols, Eq, solve

def solve_equation():
    x = symbols('x')
    equation = Eq(x + 5, 10)   # temporary example equation
    result = solve(equation)
    return result
