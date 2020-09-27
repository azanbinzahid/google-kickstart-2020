T = int(input())

for t in range(T):
    N = int(input())
    H = list(map(int, input().rstrip().split()))
    peak = 0
    for i,h in enumerate(H):
        if i==0:
            continue
        if i+1==N:
            continue
        if(H[i]>H[i-1] and H[i]>H[i+1]):
            peak +=1

    print("Case #{}: {}".format(t+1, peak))

        
