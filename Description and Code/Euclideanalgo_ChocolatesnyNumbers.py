import math

def solution(N, M):
    # The number of unique chocolates eaten before encountering a wrapper
    return N // math.gcd(N, M)
