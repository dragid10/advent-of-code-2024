import re
from pathlib import Path


def load_test_data(data_file: Path) -> str:
    instructions: str = ""
    with data_file.open("r") as file:
        instructions = data_file.read_text("utf-8")
    return instructions


def mul(x, y) -> int:
    return x * y


def parse_mul_instructions(instructions: str) -> list[str]:
    ret_instrucs: list[tuple] = []
    instruction_regex = r"(mul\(\d{1,3},\d{1,3}\))"

    valid_instructions: list = re.findall(instruction_regex, instructions, re.MULTILINE)

    return valid_instructions


if __name__ == '__main__':
    # Read in input.txt file with pathlib
    sample_file = Path("input.txt")
    test_data = load_test_data(data_file=sample_file)
    answer: int = 0

    num_pairs: list[str] = parse_mul_instructions(test_data)

    # Multiply each tuple and them sum the product
    answer = sum([eval(item) for item in num_pairs])
    print(f"Total: {answer}")
