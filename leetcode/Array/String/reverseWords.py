class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        words = []

        right = n - 1

        while right >= 0:

            while right >= 0 and s[right] == ' ':
                right -= 1

            if right < 0:
                break

            left = right

            while left >= 0 and s[left] != ' ':
                left -= 1

            words.append(s[left + 1:right + 1])

            right = left - 1
            
        return " ".join(words)
        
        
        
obj = Solution()
print(obj.reverseWords("hello world"))