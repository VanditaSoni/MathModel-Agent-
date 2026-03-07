import streamlit as st
from agent.parser import parse_problem
from agent.solver import solve_equation

st.title("AI Math Word Problem Solver")

problem = st.text_input("Enter a math word problem")

if st.button("Solve"):

    if problem.strip() == "":
        st.write("Please enter a problem.")

    else:
        try:
            # convert word problem → equation
            equation = parse_problem(problem)

            # solve equation
            answer = solve_equation(equation)

            st.write("Generated Equation:", equation)
            st.write("Answer:", answer)

        except Exception as e:
            st.write("Error:", e)