import streamlit as st
from agent.parser import parse_problem
from agent.solver import solve_equation
from agent.explain import explain_solution

st.title("AI Math Word Problem Solver")

problem = st.text_input("Enter a math word problem")

if st.button("Solve"):

    if problem.strip() == "":
        st.write("Please enter a problem.")

    else:

        try:

            # generate equations
            equations = parse_problem(problem)

            # solve equations
            solution = solve_equation(equations)

            # generate explanation
            explanation = explain_solution(problem, equations, solution)

            st.subheader("Generated Equations")
            st.code(equations)

            st.subheader("Solution")
            st.write(solution)

            st.subheader("Step‑by‑Step Explanation")
            st.write(explanation)

        except Exception as e:
            st.write("Error:", e)