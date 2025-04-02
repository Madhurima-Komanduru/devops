def solve(board, row, n, cols, diag1, diag2):
    if row == n:
        print("\n".join(" ".join(r) for r in board)); return True
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue  # Skip unsafe positions
        board[row][col] = "Q"
        if solve(board, row + 1, n, cols | {col}, diag1 | {row - col}, diag2 | {row + col}): 
            return True
        board[row][col] = "."  # Backtrack
    return False

def eight_queens(n=8):
    solve([["."] * n for _ in range(n)], 0, n, set(), set(), set())

eight_queens()
