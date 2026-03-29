class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        valid = True
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack:
                    top = stack[-1]
                else:
                    return False
                stack.pop()
                match top:
                    case '(':
                       valid = c == ')'
                    case '{':
                        valid = c == '}'
                    case '[':
                        valid = c == ']'
                    case _:
                        return False

            if not valid:
                return False
        
        if stack:
            return False

        return True                                    