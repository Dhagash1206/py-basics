class Solution:
    def subsets(self, s):

        newS = []
        temp = []

        def func(i, newS):
            if i == len(s):
                temp.append(newS.copy())
                return

            newS.append(s[i])
            func(i + 1, newS)

            newS.pop()
            func(i + 1, newS)

        func(0, newS)
        return temp


obj = Solution()
arr = [1, 2, 3]
print(obj.subsets(arr))