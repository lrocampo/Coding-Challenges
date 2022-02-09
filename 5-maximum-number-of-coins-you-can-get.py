# my solution
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        number_of_groups = len(piles) // 3 
        sorted_piles = sorted(piles, reverse=True)
        counter = 0
        maximum = 0
        for i in range(len(sorted_piles)):
            if i % 2 != 0 and counter < number_of_groups:
                maximum += sorted_piles[i]
                counter += 1
        return maximum