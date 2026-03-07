import re

def parse_problem(problem_text):

    # convert text to lowercase
    text = problem_text.lower()

    numbers = re.findall(r'\d+', text)
    numbers = [int(n) for n in numbers]

    # example: "a number plus 5 is 10"
    if "plus" in text and "is" in text and len(numbers) == 2:
        return f"x + {numbers[0]} = {numbers[1]}"

    # example: "a number minus 3 is 7"
    if "minus" in text and "is" in text and len(numbers) == 2:
        return f"x - {numbers[0]} = {numbers[1]}"

    return None