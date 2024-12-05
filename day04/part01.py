from pathlib import Path

#### NOT COMPLETE ####


SEARCH_PATTERN: list[str] = list("XMAS")


def load_test_data(data_file: Path) -> list[list[str]]:
    puzzle: list[list[str]] = []
    with data_file.open("r") as file:
        for line in file:
            puzzle.append(list(line.strip()))
    return puzzle


def east_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index][col_index + char_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def west_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index][col_index - char_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def north_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index - char_index][col_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def south_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index + char_index][col_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def northeast_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index - char_index][col_index + char_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def southeast_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index + char_index][col_index + char_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def southwest_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index + char_index][col_index - char_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


def northwest_lookup(puzzle: list[list[str]], row_index: int, col_index: int, char: str) -> bool:
    try:
        # 'M' will always be 1 away from 'X'
        # 'A' will always be 2 away from 'X'
        # 'S' will always be 3 away from 'X'
        char_index = SEARCH_PATTERN.index(char)
        if puzzle[row_index - char_index][col_index - char_index] == char:
            return True
        else:
            return False
    except IndexError:
        return False


if __name__ == '__main__':
    # Read in input.txt file with pathlib
    sample_file = Path("input-mini.txt")
    test_data = load_test_data(data_file=sample_file)
    answer: int = 0
    """ SAMPLE
         0123456789
       0 MMMSXXMASM
       1 MSAMXMSMSA
       2 AMXSXMAAMM
       3 MSAMASMSMX
       4 XMASAMXAMM
       5 XXAMMXXAMA
       6 SMSMSASXSS
       7 SAXAMASAAA
       8 MAMMMXMMMM
       9 MXMXAXMASX
       
       Read: [ROW],[COLUMN]
    """

    for row_index, row_value in enumerate(test_data):
        complete_match = 0
        for col_index, col_value in enumerate(row_value):
            if col_value != "X":
                continue

            # Look forward for remaining letters
            match_dict: dict[str, list[bool]] = {
                "north": [True, False, False, False],
                "east": [True, False, False, False],
                "south": [True, False, False, False],
                "west": [True, False, False, False],
                "northeast": [True, False, False, False],
                "southeast": [True, False, False, False],
                "southwest": [True, False, False, False],
                "northwest": [True, False, False, False],
            }

            # Go through each letter in the search pattern and see if there is a match
            for index, letter in enumerate(SEARCH_PATTERN[1::]):
                match_dict["north"][index + 1] = north_lookup(test_data, row_index, col_index, letter)
                match_dict["east"][index + 1] = east_lookup(test_data, row_index, col_index, letter)
                match_dict["south"][index + 1] = south_lookup(test_data, row_index, col_index, letter)
                match_dict["west"][index + 1] = west_lookup(test_data, row_index, col_index, letter)
                match_dict["northeast"][index + 1] = northeast_lookup(test_data, row_index, col_index, letter)
                match_dict["southeast"][index + 1] = southeast_lookup(test_data, row_index, col_index, letter)
                match_dict["southwest"][index + 1] = southwest_lookup(test_data, row_index, col_index, letter)
                match_dict["northwest"][index + 1] = northwest_lookup(test_data, row_index, col_index, letter)

            for _, val in match_dict.items():
                if all(val) is True:
                    complete_match += 1

    answer = complete_match

    print(f"Total: {answer}")

#### NOT COMPLETE ####
