class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        def func(i, pre):

            if i == len(strs):
                return pre

            while strs[i].find(pre) != 0:

                pre = pre[:-1]

                if pre == "":
                    return ""

            return func(i + 1, pre)

        return func(1, strs[0])