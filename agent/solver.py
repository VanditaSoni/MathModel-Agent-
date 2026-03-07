from sympy import symbols, Eq, solve

def solve_equation(equation_text):

    x = symbols('x')

    left, right = equation_text.split("=")

    equation = Eq(eval(left), eval(right))

    result = solve(equation)

    return result