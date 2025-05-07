def solution(A, B):
    N = len(A)
    downstream_stack = []
    survivors = 0

    for i in range(N):
        size = A[i]
        direction = B[i]

        if direction == 1:
            # Fish is going downstream; push its size onto the stack
            downstream_stack.append(size)
        else:
            # Fish is going upstream; fight with downstream fish
            while downstream_stack:
                if downstream_stack[-1] > size:
                    # Upstream fish gets eaten
                    break
                else:
                    # Downstream fish gets eaten
                    downstream_stack.pop()
            else:
                # No downstream fish left; upstream fish survives
                survivors += 1

    # Remaining downstream fish in the stack are survivors
    return survivors + len(downstream_stack)
