class Solution:
    def commonChars(self, words):
        s = set(min(words, key=len))
        r = []

        for c in s:
            k = min(w.count(c) for w in words)
            r.extend([c] * k)

        return r
