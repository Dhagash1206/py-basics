class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:

            s = carry

            if i >= 0:
                s += int(a[i])
                i -= 1

            if j >= 0:
                s += int(b[j])
                j -= 1

            ans.append(str(s % 2))
            carry = s // 2

        return "".join(ans[::-1])