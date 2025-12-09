# A left rotation operation on an array shifts each of the array’s elements unit to the left. For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

# Sample Input

# STDIN      Function
# -----      --------
# 5 4         n = 5 d = 4
# 1 2 3 4 5  arr = [1, 2, 3, 4, 5]
# Sample Output

# 5 1 2 3 4


class Solution(object):
    # due to inside of class an extra paramaters self is passed - it is like constructor
    def rotateLeft(self, d, arr):
        # Write your code here
        for i in range(d):
            x = arr[0]
            arr.remove(x)
            arr.append(x)
        return arr


def main():
    s = Solution()
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = s.rotateLeft(d, arr)
    print(result)


main()
