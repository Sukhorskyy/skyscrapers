'''
Skyscrapers game
The module checks whether the entered combination is winning
Repository address on GitHub: https://github.com/Sukhorskyy/skyscrapers.git
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open('check.txt', mode='r', encoding='utf-8') as data:
        content = data.readlines()
    for i in range(len(content)):
        content[i] = content[i].strip()
    return content


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = list(input_line)
    del input_line[0]
    del input_line[-1]
    counter = 1
    max_el = input_line[0]
    for i in range(1, len(input_line)):
        if input_line[i] > max_el:
            counter = counter + 1
        max_el = max(input_line[:i])
    if counter == pivot:
        return True
    else:
        return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for i in range(len(board)):
        board[i] = board[i].strip('*')
    for i in range(len(board)):
        try:
            board[i] = int(board[i])
        except ValueError:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for i in range(len(board)):
        board[i] = board[i][1:-1]
        board[i] = list(board[i])
    for i in range(len(board)):
        board_set = set(board[i])
        if len(board[i]) != len(board_set):
            return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(len(board)):
        if board[i][0] != '*':
            if left_to_right_check(board[i], int(board[i][0])) == False:
                return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for i in range(len(board)):
        board[i] = board[i][1:-1]
        board[i] = list(board[i])
    new_board = [[0 for i in range(len(board))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[j][i] = board[i][j]
    for i in range(len(new_board)):
        board_set = set(new_board[i])
        if len(new_board[i]) != len(board_set):
            return False
    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if check_not_finished_board(board) == True:
        if (check_uniqueness_in_rows(board) == True) and \
            (check_horizontal_visibility(board) == True) and \
                (check_columns(board) == True):
            return True


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
    import doctest
    doctest.testmod()
