import os
from google import genai
from dotenv import load_dotenv

# load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyCYlwFhrcF6oPI4MZrBDOnjgGBPShhV9y8"))

def parse_problem(problem_text):

    prompt = f"""
Convert the following math word problem into a mathematical equation using variable x.

Problem:
{problem_text}

Rules:
- Only return the equation
- Use variable x
- Do not explain

Example:
Input: A number plus 5 is 10
Output: x + 5 = 10
"""
    # example: "a number plus 5 is 10"
    if "plus"or "add" in text and "is" in text and len(numbers) == 2:
        return f"x + {numbers[0]} = {numbers[1]}"

    # example: "a number minus 3 is 7"
    if "minus" or "subtract" in text and "is" in text and len(numbers) == 2:
        return f"x - {numbers[0]} = {numbers[1]}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    equation = response.text.strip()

    return equation