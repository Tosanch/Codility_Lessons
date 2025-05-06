def solution(A):
    east_cars = 0
    passing_pairs = 0

    for car in A:
        if car == 0:
            east_cars += 1
        else:  # car == 1 (westbound)
            passing_pairs += east_cars
            if passing_pairs > 1_000_000_000:
                return -1

    return passing_pairs
