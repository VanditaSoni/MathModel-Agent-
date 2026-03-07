import streamlit as st
from agent.parser import parse_problem
from agent.solver import solve_equation

st.title("MathModel Agent")

problem = st.text_input("Enter a math problem")

if st.button("Solve"):

    equation = parse_problem(problem)
    answer = solve_equation()

    st.write("Equation:", equation)
    st.write("Answer:", answer)
