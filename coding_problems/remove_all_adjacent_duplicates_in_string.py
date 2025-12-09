
# Input: s = "abbaca"
# Output: "ca"

# Input: s = "azxxzy"
# Output: "ay"

class Solution(object):
    # due to inside of class an extra paramaters self is passed - it is like constructor
    def removeDuplicates(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)


def main():
    s = Solution()
    print(s.removeDuplicates("abbacd"))
    print(s.removeDuplicates("azxxzy"))


main()


# for debugging purpose

# class Solution(object):
#     def removeDuplicates(self, S):
#         res = []
#         for c in S:
#             print(F"res[]  {res}, character {c}")
#             if res and res[-1] == c:
#                 print(F"res[-1] {res[-1]}")
#                 print("if block")
#                 res.pop()
#             else:
#                 print("else block")
#                 res.append(c)
#         return "".join(res)


# def main():
#     s = Solution()
#     print(s.removeDuplicates("abbacd"))
#     print("----------------------------------------------")
#     print(s.removeDuplicates("azxxzy"))


# main()
