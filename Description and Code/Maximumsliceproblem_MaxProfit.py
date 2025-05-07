def solution(A):
    if not A:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit
