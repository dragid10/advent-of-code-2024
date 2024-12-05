import re
from pathlib import Path

#### DID NOT COMPLETE ####

def load_test_data(data_file: Path) -> str:
    instructions: str = ""
    with data_file.open("r") as file:
        instructions = data_file.read_text("utf-8")
    return instructions


def parse_mul_instructions(instructions: str) -> list[tuple]:
    ret_instrucs: list[tuple] = []
    instruction_regex = r"(mul\(\d{1,3},\d{1,3}\))"

    valid_instructions: list = re.findall(instruction_regex, instructions, re.MULTILINE)

    for instruction in valid_instructions:
        instruction = instruction.replace("mul", "").replace("(", "").replace(")", "")
        num_a, num_b = instruction.split(",")
        ret_instrucs.append((int(num_a), int(num_b)))

    return ret_instrucs


if __name__ == '__main__':
    # Read in input.txt file with pathlib
    sample_file = Path("input.txt")
    test_data = load_test_data(data_file=sample_file)
    answer: int = 0

    num_pairs: list[tuple] = parse_mul_instructions(test_data)

    # Multiply each tuple and them sum the product
    answer = sum([x * y for x, y in num_pairs])
    print(f"Total: {answer}")

#### DID NOT COMPLETE ####
