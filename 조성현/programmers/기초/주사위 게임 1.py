def solution(a, b):
    if a%2==1 and b%2==1:
        return a**2 + b**2
    if a%2==1 or b%2==1:
        return 2*(a+b)
    return abs(a-b)