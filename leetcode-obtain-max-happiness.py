class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse = True)
        sum = 0

        for i in range k : 
            sum = happiness[i]
            happiness = [element - 1 if element > 0 else element for element in happiness]
            return if happiness[i + 1] = 0


        return happiness
            
