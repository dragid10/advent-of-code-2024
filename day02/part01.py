from pathlib import Path


def load_test_data(data_file: Path) -> list[list]:
    """
    48 46 43 42 40 38
    87 84 83 80 77 76
    """
    unusual_data: list = []
    with data_file.open("r") as file:
        for line in file:
            # Turn each line of numbers into a list of numbers
            raw_report_str: list[str] = line.split(" ")

            # Convert all strings to ints (to do math)
            raw_report_int: list[int] = [int(level) for level in raw_report_str]

            # Add each report list to the data list
            unusual_data.append(raw_report_int)
    return unusual_data


def levels_increasing(report: list[int]) -> bool:
    for index, current_level in enumerate(report[1::]):
        if current_level < report[index]:
            return False
    return True


def levels_decreasing(report: list[int]) -> bool:
    for index, current_level in enumerate(report[1::]):
        if current_level > report[index]:
            return False
    return True


def levels_differ_appropriately(report: list[int]) -> bool:
    """
    2. Any two adjacent levels differ by at least one and at most three.
    :param report:
    :return:
    """
    for index, current_level in enumerate(report[1::]):
        level_difference: int = abs(current_level - report[index])
        # Check if level difference is between 1 and 3 (both inclusive)
        if level_difference not in range(1, 4):
            return False
    return True


def is_report_safe(report: list[int]) -> bool:
    """ A report is considered safe when:
    1. The levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least one and at most three.

    :param report: List of numbers (levels)
    :return: bool - True if safe, False if not
    """

    """
    Dedupe:
     48 46 43 42 40 38 -> safe
     87 84 83 80 77 76 -> safe
     87 87 83 80 77 76 -> unsafe (condition 1)
     87 84 83 87 77 76 -> unsafe (condition 1)
     87 84 83 87 77 76
    """

    # If there are any duplicate numbers, then we know it fails one of the conditions
    contains_duplicates: bool = len(set(report)) != len(report)
    if contains_duplicates:
        return False

    # Actually check the conditions

    # Condition 1 check
    passes_condition_1 = levels_increasing(report) or levels_decreasing(report)

    if not passes_condition_1:
        return False

    # Condition 2 check
    passes_condition_2 = levels_differ_appropriately(report)
    return passes_condition_1 and passes_condition_2


if __name__ == '__main__':
    # Read in input.txt file with pathlib
    sample_file = Path("input.txt")
    test_data = load_test_data(data_file=sample_file)

    answer: int = 0

    # Loop through all reports in data
    for report in test_data:
        # Check if report is safe
        safe_report = is_report_safe(report=report)

        if safe_report:
            answer += 1

    print(f"Total: {answer}")
