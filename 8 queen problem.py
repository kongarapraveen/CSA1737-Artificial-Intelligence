def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    """ Use backtracking to solve the N-Queens problem """
    # Base case: If all queens are placed, return true
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place rest of the queens
            if solve_queens(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, return false
    return False

def print_board(board):
    """ Print the board """
    for row in board:
        print(row)

def solve_n_queens(n):
    """ Initialize the board and solve the N-Queens problem """
    board = [[0] * n for _ in range(n)]

    if not solve_queens(board, 0):
        print("No solution exists")
        return False

    print("Solution:")
    print_board(board)
    return True

# Example usage:
if __name__ == "__main__":
    n = 8  # Number of queens (size of the chessboard)
    solve_n_queens(n)
