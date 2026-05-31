class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, freq):
            if len(path) == len(nums):
                ans.append(list(path))
                return

            for num in freq:
                if freq[num] > 0:
                    path.append(num)
                    freq[num] -= 1

                    backtrack(path, freq)

                    path.pop()
                    freq[num] += 1

        backtrack([], Counter(nums))
        return ans