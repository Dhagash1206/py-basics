class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                p = p + i

        return p == p[::-1]