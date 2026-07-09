class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        out = [0 for _ in temperatures]
        temp_stack: list[int] = []
        index_stack: list[int] = []

        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while temp_stack and current_temp > temp_stack[-1]:
                temp_stack.pop()
                old_index = index_stack.pop()
                out[old_index] = i - old_index

            temp_stack.append(current_temp)
            index_stack.append(i)

        return out