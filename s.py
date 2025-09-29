

N = 8  # Chessboard size (8x8)

def is_safe(x, y, board):
    """Check if knight can move to board[x][y]."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_board(board):
    for row in board:
        print(" ".join(f"{cell:2}" for cell in row))
    print("\n")

def solve_knight_tour():
    # Initialize board
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Possible knight moves
    moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
    moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Starting position
    board[0][0] = 0  

    pos = 1  # Step counter

    if not solve_util(0, 0, moves_x, moves_y, board, pos):
        print("Solution does not exist")
    else:
        print_board(board)

def solve_util(x, y, moves_x, moves_y, board, pos):
    # If all squares are visited
    if pos == N * N:
        return True

    # Try all next moves
    for i in range(8):  # Loop over 8 possible moves
        new_x, new_y = x + moves_x[i], y + moves_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos
            if solve_util(new_x, new_y, moves_x, moves_y, board, pos + 1):
                return True
            # Backtrack
            board[new_x][new_y] = -1  
    return False


if __name__ == "__main__":
    solve_knight_tour()
