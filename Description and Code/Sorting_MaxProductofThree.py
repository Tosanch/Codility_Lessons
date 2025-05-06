def solution(A):
    # Sort the array
    A.sort()

    # Calculate the two possible maximal products
    product1 = A[-1] * A[-2] * A[-3]  # Three largest numbers
    product2 = A[0] * A[1] * A[-1]  # Two smallest numbers and the largest number

    # Return the maximum product
    return max(product1, product2)