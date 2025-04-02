def print_board(b):
    print("\n".join([" | ".join(row) for row in b]) + "\n")

def check(b, p):
    return any(all(c == p for c in r) for r in b) or \
           any(all(b[r][c] == p for r in range(3)) for c in range(3)) or \
           all(b[i][i] == p for i in range(3)) or all(b[i][2 - i] == p for i in range(3))

b, p = [[" "] * 3 for _ in range(3)], "X"
for _ in range(9):
    print_board(b)
    r, c = map(int, input(f"Player {p}, enter row and col (0-2): ").split())
    if b[r][c] != " ":
        print("Cell taken! Try again."); continue
    b[r][c] = p
    if check(b, p):
        print_board(b); print(f"Player {p} wins! 🎉"); break
    p = "O" if p == "X" else "X"
else:
    print_board(b); print("It's a draw! 🤝")
