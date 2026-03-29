class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = {"+", "-", "*" , "/"}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in exp:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                match tokens[i]:
                    case "+":
                        stack.append(b + a)
                        print(b, "+", a, "=" , b + a)
                    case "-":
                        stack.append(b - a)
                        print(b, "-", a, "=" , b - a)
                    case "*":
                        stack.append(b * a)
                        print(b, "*", a, "=" , b * a)
                    case "/":
                        stack.append(int(b / a))
                        print(b, "/", a, "=" , int(b / a))
        return stack.pop()


        

        


