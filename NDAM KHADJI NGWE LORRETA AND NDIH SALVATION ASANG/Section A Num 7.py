import sys

class Queen:
    """
    Class to represent a queen on the chessboard.
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col

def is_safe(board, row, col):
    """
    Check if placing a queen at position (row, col) is safe.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i].col == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i].col == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i].col == j:
            return False

    return True

def solve_n_queens(n):
    """
    Solve the N-Queens problem for a given board size.
    """
    # Initialize an empty board
    board = [None] * n

    def helper(row):
        """
        Helper function to recursively solve the N-Queens problem.
        """
        # Base case: if all queens are placed, print the solution
        if row == n:
            print([[q.row, q.col] for q in board])
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                # Place the queen at (row, col)
                board[row] = Queen(row, col)
                # Recur for the next row
                helper(row + 1)
                # Backtrack: remove the queen from (row, col)
                board[row] = None

    # Start recursion from the first row
    helper(0)

# Main function
if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the argument is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem for the given board size
    solve_n_queens(N)
