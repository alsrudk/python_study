import math
def get_lcm(num1, num2):
    return (num1*num2)//math.gcd(num1, num2)

def solution(arr):
    answer = 0
    for i in range(len(arr)-1):
        print(arr[i], arr[i+1])
        answer = get_lcm(arr[i], arr[i+1])
        arr[i+1] = answer
    
    return answer
