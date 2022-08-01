# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_array = [i**2 for i in nums]
        return sorted(square_array)
