T = int(input())
for t in range(T):
    S, Ra, Pa, Rb, Pb, C = map(int, input().split())
    block = []
    for c in range(C):
        Ri, Pi = map(int, input().split())
        block.append([Ri,Pi])
    ans = 0
    if C == 2:
        ans = 0
    elif C == 0:
        if (Ra==2 and Pa==2):
            ans = 1
        elif (Rb==2 and Pb==2):
            ans = -1
        else: 
            ans = 2
    elif C==1:
        if(block[0][0]==2 and block[0][1]==2):
            ans = 0
        elif(Rb==2 and Pb==2):
            ans = -1
        else:
            ans = 1
    print("Case #{}: {}".format(t+1, ans))