class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # create our incrementor
        i = 0

        # loop through all dynamic elements
        while i < len(arr)-1:
            # if the character is a zero
            if arr[i] == 0:
                # remove the last item from the array
                arr.pop()

                # insert a zero in front of current elemen
                arr.insert(i+1, 0)
                # move one place forward
                i += 1
            # increment to the next character
            i += 1
