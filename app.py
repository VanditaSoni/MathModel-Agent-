import streamlit as st
from agent.parser import parse_problem
from agent.solver import solve_equation

st.title("MathModel Agent")

problem = st.text_input("Enter a word problem")

if st.button("Solve"):

    equation = parse_problem(problem)

    if equation:
        answer = solve_equation(equation)

        st.write("Generated Equation:", equation)
        st.write("Answer:", answer)

    else:
        st.write("Sorry, I could not understand the problem.")