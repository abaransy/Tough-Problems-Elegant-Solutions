# Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature. If there is no
# future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
#brute force
#         res = []

#         for i in range(len(T)):
#             j = i

#             while j < len(T) and T[j] <= T[i]:
#                 j += 1

#             wait = j - i if j < len(T) else 0

#             res.append(wait)

#         return res

#better, stack based solution

        res = [0] * len(T)
        idx_stack = []

        for i in range(len(T)):
            while idx_stack and T[i] > T[idx_stack[-1]]:
                j = idx_stack.pop()
                res[j] = i - j

            idx_stack.append(i)

        return res
