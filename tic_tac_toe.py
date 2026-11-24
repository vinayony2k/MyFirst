"""A simple two-player, command-line Tic-Tac-Toe game."""


def display_board(board):
    """Print the board, showing square numbers in empty cells."""
    cells = [str(value) if value != " " else str(index + 1)
             for index, value in enumerate(board)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---|---|---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---|---|---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} \n")


def has_won(board, mark):
    """Return True if mark occupies a complete row, column, or diagonal."""
    winning_lines = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    return any(all(board[index] == mark for index in line)
               for line in winning_lines)


def play():
    """Run a two-player Tic-Tac-Toe game in the terminal."""
    board = [" "] * 9
    current_mark = "Y"

    print("Welcome to Tic-Tac-Toe!")
    print("Choose a square by entering its number (1-9).")

    while True:
        display_board(board)
        choice = input(f"Player {current_mark}, choose a square: ").strip()

        if choice not in "123456789" or len(choice) != 1:
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1
        if board[position] != " ":
            print("That square is already taken. Choose another one.")
            continue

        board[position] = current_mark

        if has_won(board, current_mark):
            display_board(board)
            print(f"Player {current_mark} wins!")
            break

        if " " not in board:
            display_board(board)
            print("It's a draw!")
            break

        current_mark = "S" if current_mark == "Y" else "Y"


if __name__ == "__main__":
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print("\nGame ended.")
