import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def parse_problem(problem_text):

    prompt = f"""
Convert the following math word problem into mathematical equations.

Rules:
- Use variables x and y if needed
- If two unknown numbers exist, create two equations
- Return only equations
- If multiple equations, place them on separate lines
- Do not explain anything

Example:

Problem:
Two numbers add to 20 and differ by 4

Output:
x + y = 20
x - y = 4

Problem:
{problem_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    equations = response.text.strip()

    return equations