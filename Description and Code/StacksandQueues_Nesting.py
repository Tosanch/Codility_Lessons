def solution(S):
    balance = 0
    for char in S:
        if char == '(':
            balance += 1
        else:  # char == ')'
            balance -= 1
            if balance < 0:
                return 0  # more ')' than '(' at some point
    return 1 if balance == 0 else 0
