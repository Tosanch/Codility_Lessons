def solution(X, Y, D):
    # Calculate the distance the frog needs to cover
    distance = Y - X

    # Compute the minimal number of jumps using ceiling division
    jumps = (distance + D - 1) // D

    return jumps
