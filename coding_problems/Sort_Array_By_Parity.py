class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resEven = []
        resOdd = []
        for i in nums:
            if i % 2 == 0:
                resEven.append(i)
            else:
                resOdd.append(i)
        return resEven + resOdd


def main():
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))


main()

# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.


# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
