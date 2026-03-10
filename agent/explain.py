import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def explain_solution(problem, equations, solution):

    prompt = f"""
Explain step-by-step how the following math problem is solved.

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