def solution(H):
    stack = []
    block_count = 0

    for height in H:
        # Remove all taller blocks
        while stack and stack[-1] > height:
            stack.pop()

        # If stack is empty or current height is different, need a new block
        if not stack or stack[-1] < height:
            block_count += 1
            stack.append(height)

    return block_count
