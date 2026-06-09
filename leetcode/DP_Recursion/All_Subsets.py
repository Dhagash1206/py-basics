class Solution:
    def subsets(self, s: str):

        ans = []

        def func(i, subset):

            if i == len(s):
                ans.append(subset)
                return

            func(i + 1, subset)

            func(i + 1, subset + s[i])

        func(0, "")
        
        ans = "\n".join(ans)

        return ans



obj = Solution()

print(obj.subsets("abcde"))