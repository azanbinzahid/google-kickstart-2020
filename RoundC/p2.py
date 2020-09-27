import math

global A

def SubArraySum(a):
    """Compute sum of all subarrays of a, multiplied by its last element"""
    w, h = len(a), len(a)
    Matrix = [[0 for x in range(w)] for y in range(h)] 
    res = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if(i == 0 and j == 0):
                Matrix[i][j] = a[i] 
            else:    
                Matrix[i][j] = Matrix[i][j-1] + a[j]
            
            if chksq(Matrix[i][j]):
                res+=1
            
    return res


def chksq(number):
    if number < 0:
        number*=-1
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

for t in range(int(input())):
    global A
    N = int(input())
    A = list(map(int, input().split()))
    count = SubArraySum(A)
    print("Case #{}: {}".format(t+1, count))
