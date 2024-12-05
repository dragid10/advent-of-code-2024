import collections
from collections import Counter
from pathlib import Path


def load_test_data(data_file: Path) -> tuple[list, list]:
    group1_list: list[int] = list()
    group2_list: list[int] = list()
    with data_file.open("r") as file:
        for line in file:
            line_list = line.split("   ")
            group1_list.append(int(line_list[0]))
            group2_list.append(int(line_list[1]))
    return group1_list, group2_list


if __name__ == '__main__':
    # Read in input.txt file with pathlib
    sample_file = Path("input.txt")
    left_list, right_list = load_test_data(data_file=sample_file)

    # Sort each list
    left_list.sort()
    right_list.sort()

    # Get rid of duplicates in left list
    left_list: set = set(left_list)

    # Count frequency of occurrence
    right_list_freq: Counter = Counter(right_list)

    # Remove numbers that aren't in left list
    for key, val in right_list_freq.copy().items():
        if key not in left_list:
            del right_list_freq[key]

    answer = 0
    for key, value in right_list_freq.items():
        answer += (key * value)

    # # zip lists together
    # zipped_list = zip(left_list, right_list)
    #
    # # Get the difference between each element in the zipped list
    # diff_list = [abs(x - y) for x, y in zipped_list]
    #
    # # Get the sum of the differences
    # answer = sum(diff_list)

    print(f"Total distances: {answer}")
