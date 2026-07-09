class Solution:
    def apply_operator(self, num2: int, num1: int, operator: str) -> int:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(num1 / num2)
            case _:
                raise NotImplementedError(operator)

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric() or (token[0] == "-" and token[1:].isnumeric()):
                # if valid wasn't guaranteed: check len(stack) < 2
                stack.append(int(token))
            else:
                # if valid wasn't guaranteed: check len(stack) == 2
                stack.append(self.apply_operator(stack.pop(), stack.pop(), token))

        # if valid wasn't guaranteed: check len(stack) == 1
        return stack.pop()
