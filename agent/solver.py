import re
from sympy import symbols, Eq, solve

def format_equation(expr):
    """
    Convert expressions like 2x → 2*x
    """
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    return expr


def solve_equation(equations_text):

    x, y = symbols('x y')

    equations = []

    lines = equations_text.split("\n")

    for line in lines:

        if "=" in line:

            left, right = line.split("=")

            left = format_equation(left.strip())
            right = format_equation(right.strip())

            eq = Eq(eval(left), eval(right))

            equations.append(eq)

    # single equation
    if len(equations) == 1:
        result = solve(equations[0])
        return result

    # system of equations
    else:
        result = solve(equations, (x, y))
        return result[0]