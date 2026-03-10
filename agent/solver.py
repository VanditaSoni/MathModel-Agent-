from sympy import symbols, Eq, solve

def solve_equation(equations_text):

    x, y = symbols('x y')

    equations = []

    lines = equations_text.split("\n")

    for line in lines:

        if "=" in line:

            left, right = line.split("=")

            left = left.strip()
            right = right.strip()

            eq = Eq(eval(left), eval(right))

            equations.append(eq)

    # single equation
    if len(equations) == 1:
        result = solve(equations[0])
        return result

    # system of equations
    else:
        result = solve(equations, (x, y))
        return result