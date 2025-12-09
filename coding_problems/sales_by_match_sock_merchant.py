# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.

# Sample Input
#              9
#              10 20 20 10 10 30 50 10 20
# Sample Output
#              3


class Solution(object):
    # due to inside of class an extra paramaters self is passed - it is like constructor
    def sockMerchant(self, n, ar):
        total_pairs = 0
        pairsArray = []
        set_arr = set(ar)
        for i in set_arr:
            pair_count = ar.count(i)//2
            pairsArray.append(pair_count)
            total_pairs += pair_count
        return total_pairs, pairsArray


def main():
    s = Solution()
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    tp, p = s.sockMerchant(n, arr)
    print(tp)


main()
