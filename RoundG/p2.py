T = int(input())

# stackoverflow
def get_rows(grid):
    return [[c for c in r] for r in grid]

def get_cols(grid):
    return zip(*grid)

def get_backward_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]
# ------------------

for t in range(T):
    N = int(input())
    matrix = []
    for n in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    ans = max(map(sum, get_backward_diagonals(matrix)))
    print("Case #{}: {}".format(t+1, ans))
