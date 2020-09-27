T = int(input())

def multiples(m,D):
    return D - D % m

for t in range(T):
    N, D = map(int, input().rstrip().split())
    X = list(map(int, input().rstrip().split()))
    last = multiples(X[-1],D)
    for x in reversed(X[:-1]):
        last = multiples(x,last)
    print("Case #{}: {}".format(t+1, last))

        
