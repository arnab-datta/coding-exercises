class Solution(object):
    # due to inside of class an extra paramaters self is passed - it is like constructor
    def generateParenthesis(self, n):
        # only add open paranthesis if open < n
        # only add closing paranthesis  if closed < open
        # valid if open == closed == n
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0, 0)
        return res


def main():
    s = Solution()
    print(s.generateParenthesis(3))


main()


# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
