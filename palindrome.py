import math
def palindrome(num):
    num=str(num)
    if num==num[::-1]:
        return True
    return False

def factors(num):
    count=[]
    for i in range(1, int(math.sqrt(num)) + 1):
        if(num%i == 0):
            if(num/i == i):
                count.append(i)
            else:
                count.append(i)
                count.append(num//i)
    return count

def pFactor(num):
    result = []
    fac = factors(num)
    for i in fac:
        if palindrome(i):
            result.append(i)
    return len(result)
testCase = int(input())
inputs = []
for i in range(testCase):
    num = input()
    inputs.append(int(num))
count=1
for obj in inputs:
    print(f'Case #{count}: {pFactor(obj)}')
    count+=1
