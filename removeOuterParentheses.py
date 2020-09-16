def removeOuterParentheses(S: str) -> str:
    new = []
    [new.append(char) for char in S]
    saved = int
    for i, stupid in enumerate(new):
        if stupid == '(':
            new.remove(stupid)
        elif stupid == ')':
            new.remove(stupid)
    return ''.join(new)


print(removeOuterParentheses("(()())(())"))
