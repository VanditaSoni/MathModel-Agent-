import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def explain_solution(problem, equations, solution):

    prompt = f"""
Explain step-by-step how the following math problem is solved.
Solution should be not too small and not too long keep it easy and medium detailed.
Explain the questions asked in the problem and how they relate to the equations and solution.
Explain the final solution and how it answers the question asked in the problem.

Problem:
{problem}

Equations:
{equations}

Solution:
{solution}

Give clear numbered steps.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()