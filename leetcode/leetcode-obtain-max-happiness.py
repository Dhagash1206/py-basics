class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int):
        happiness.sort(reverse=True)

        total_happiness = 0

        for i in range(k):
            current_happiness = max(happiness[i] - i, 0)
            total_happiness += current_happiness

        return total_happiness