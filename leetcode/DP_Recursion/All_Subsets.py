class Solution:
    def subsets(self, s: str):

        newS = []
        temp = []

        def func(i, newS):
            
            if i == len(s):
                temp.append(newS.copy())
                return
            
            
            newS.append(s[i])
            func(i+1,newS)
            
            
            newS.pop()
            func(i+1,newS)
            
            
            return temp[]
            
        return func(0,newS)
            



obj = Solution()
arr  = [1,2,3]
print(obj.subsets(arr))