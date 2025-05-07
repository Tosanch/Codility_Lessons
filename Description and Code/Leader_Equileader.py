def solution(A):
    size = 0
    candidate = None

    # Step 1: Find the candidate for leader using Boyer-Moore voting algorithm
    for value in A:
        if size == 0:
            candidate = value
            size = 1
        else:
            size += 1 if value == candidate else -1

    # Step 2: Verify if the candidate is a true leader
    count = A.count(candidate)
    if count <= len(A) // 2:
        return 0  # No leader, so no equi leaders

    leader = candidate
    equi_leaders = 0
    left_count = 0
    total = len(A)

    # Step 3: Iterate through the array to find equi leaders
    for index in range(total):
        if A[index] == leader:
            left_count += 1

        left_size = index + 1
        right_size = total - left_size

        if (left_count > left_size // 2 and
            (count - left_count) > right_size // 2):
            equi_leaders += 1

    return equi_leaders
