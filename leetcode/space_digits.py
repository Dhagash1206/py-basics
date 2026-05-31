class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        # number into string
        nums = map(str, nums)

        # Join all num to one string
        new_str = "".join(nums)

        # Add spaces between every digit
        spaced_str = new_str.replace("", " ")[1:-1]

        # Split digits into list of strings
        nums = spaced_str.split()

        # string to integers
        nums = list(map(int, nums))

        return nums

# Method 2

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            tmp = []
            while x > 0:
                tmp.append(x % 10)
                x //= 10
            res.extend(tmp[::-1])
        return res