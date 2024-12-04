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
    group1, group2 = load_test_data(data_file=sample_file)

    # Sort each list
    group1.sort()
    group2.sort()

    # zip lists together
    zipped_list = zip(group1, group2)

    # Get the difference between each element in the zipped list
    diff_list = [abs(x - y) for x, y in zipped_list]

    # Get the sum of the differences
    sum_diff = sum(diff_list)

    print(f"Total distances: {sum_diff}")
