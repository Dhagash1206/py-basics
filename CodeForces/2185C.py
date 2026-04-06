import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    s = sorted(set(a))
    
    best = cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1] + 1:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
    
    print(best)