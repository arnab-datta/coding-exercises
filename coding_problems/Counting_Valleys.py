# Sample Input
# 8
# UDDDUDUU
# Sample Output
# 1

# 12
# DDUUDDUDUUUD
# 2

# Input Format
# The first line contains an integer, , denoting the number of steps in Gary’s hike.
# The second line contains a single string of characters. Each character belongs to {U, D} (where U indicates a step up and D indicates a step down), and the i(th) cin the string describes Gary’s i(th) step during the hike.

# A mountain is a non-empty sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a non-empty sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

# If we represent _ as sea level, a step up as / , and a step down as \ , Gary’s hike can be drawn as:
# _/\      _
#    \    /
#     \/\/


class Solution(object):
    # due to inside of class an extra paramaters self is passed - it is like constructor
    def countingValley(self, steps, path):
        level = valley = 0
        for i in path:
            if i.lower() == 'u':
                level += 1
            elif i.lower() == 'd':
                if level == 0:
                    valley += 1
                level -= 1
        return valley


def main():
    s = Solution()
    steps = int(input())
    path = input()
    print(s.countingValley(steps, path))


main()
