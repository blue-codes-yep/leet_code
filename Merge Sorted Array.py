class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]

        nums1.sort()


# Time Complexity: O((N + M)log(N+M)), where N and M are the size of array A[] and B[]
# Space Complexity: O(N), built-in sort takes space
