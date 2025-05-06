# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Convert N to binary and strip the '0b' prefix
    binary = bin(N)[2:]

    max_gap = 0
    current_gap = 0
    in_gap = False

    for bit in binary:
        if bit == '1':
            if in_gap:
                max_gap = max(max_gap, current_gap)
            # Start a new potential gap
            current_gap = 0
            in_gap = True
        elif in_gap:
            current_gap += 1

    return max_gap
