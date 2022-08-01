class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Turn the list of ints into a string
        list_nums = map(str, nums)
        count = 0

        # If the length of the string is even, then increase the count.
        for s in list_nums:
            if len(s) % 2 == 0:
                count += 1
        return count
