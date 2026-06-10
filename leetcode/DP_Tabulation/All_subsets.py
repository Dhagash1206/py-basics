class Solution:
    def subsets(self, s):

        dp = [[]]

        for i in range(len(s)):

            current_subsets = []

            for subset in dp:
                current_subsets.append(subset + [s[i]])

            dp.extend(current_subsets)

        return dp


obj = Solution()

arr = ["a", "b", "c"]

print(obj.subsets(arr))