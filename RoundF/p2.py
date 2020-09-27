import math

T = int(input())
for c in range(T):
    N, K = map(int, input().split())
    time = []
    for n in range(N):
        S, E = map(int, input().split())
        time.append([S,E])
    
    time.sort(key=lambda x: x[0])
    robotCount = 0
    robotCurrent = time[0][0]
    for t in time:
        if (robotCurrent<t[0]):
            robotCurrent = t[0]

        factor = t[1]-robotCurrent
        if factor>0:
            calc = math.ceil(factor/K)
            robotCount+= calc
            robotCurrent +=K*calc


    ans = robotCount
    print("Case #{}: {}".format(c+1, ans))