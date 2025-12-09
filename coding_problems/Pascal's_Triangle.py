class Solution(object):
    # due to inside of class an extra paramaters self is passed - it is like constructor
    def pascalsTriangle(self, n):
        res = [[1]]

        for i in range(n-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)

        return res


def main():
    s = Solution()
    print(s.pascalsTriangle(5))


main()


# 118. Pascal's Triangle
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
