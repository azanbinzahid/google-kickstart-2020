global A

def countdown(itr, k):
    ret = False

    for i in range(k, 0, -1):
        if itr > len(A)-1:
            return False
        if(A[itr]!=i):
            return False
        itr+=1
        ret = True
    return ret


for t in range(int(input())):
    N, k = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i, v in enumerate(A):
        if v == k:
            if countdown(i, k):
                count+=1
    print("Case #{}: {}".format(t+1, count))
