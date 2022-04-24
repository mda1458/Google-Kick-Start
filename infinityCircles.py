import math
def getArea(r):
    return math.pi*r**2

def infinity(R,A,B):
    sum=0
    while R!=0:
        sum+=(getArea(R)+getArea(R*A))
        R = R*A//B
    return sum
    
testCase = int(input())
inputs = []
for i in range(testCase):
    R,A,B = input().split()
    inputs.append((int(R), int(A), int(B)))
count=1
for i in inputs:
    print(f'Case #{count}: {infinity(i[0],i[1],i[2])}')
    count+=1

