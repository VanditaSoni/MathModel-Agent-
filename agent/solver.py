from sympy import symbols, Eq, solve


def solve_equation(equation_text):
    """
    Solve equation using SymPy
    """

    x = symbols('x')

    # split equation
    left, right = equation_text.split("=")

    left = left.strip()
    right = right.strip()

    equation = Eq(eval(left), eval(right))

    result = solve(equation)

    return result[0]