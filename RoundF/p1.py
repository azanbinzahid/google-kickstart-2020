import math
T = int(input())
for t in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans= []
    store = {}
    for i,a in enumerate(A):
        k = math.ceil(a/X)
        if (k not in store):
            store[k] = []
        store[k].append(i)
    for i in sorted(store.keys()):
        for v in store[i]:
            ans.append(v)
        
    print("Case #{}: {}".format(t+1, " ".join(str(x+1) for x in ans)))