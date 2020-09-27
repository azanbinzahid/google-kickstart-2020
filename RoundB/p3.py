T = int(input())

for t in range(T):
    S = input()
        
    ans = {
        "N" : 0,
        "S" : 0,
        "W" : 0,
        "E" : 0
    }

    stack = []
    stack_count = 1
    for s in S:
        if s.isdigit():
            stack_count*=int(s)
            stack.append(int(s))
        elif s=='(':
            pass
        elif s==')':
            stack_count//=stack.pop()
        else:
            ans[s] = ans[s] + stack_count
    
    S = "" 
    mx = pow(10,9)

    y = ans['S'] - ans['N'] + 1
    x = ans['E'] - ans['W']  + 1

    if (y>0):
        y = y % mx
    elif (y<=0):
        y = mx + y
    
    if (x>0):
        x = x % mx

    elif (x<=0):
        x = mx + x
    print("Case #{}: {} {}".format(t+1, x,y))       
