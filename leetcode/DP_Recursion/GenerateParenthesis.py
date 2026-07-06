class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def func(curr, open_cnt, close_cnt):
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if open_cnt < n:
                func(curr + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                func(curr + ")", open_cnt, close_cnt + 1)

        func("", 0, 0)

        return ans