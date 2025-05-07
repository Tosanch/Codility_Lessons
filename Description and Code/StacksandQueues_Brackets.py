def solution(S):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in S:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_map[char]:
                return 0
            stack.pop()

    return 1 if not stack else 0
