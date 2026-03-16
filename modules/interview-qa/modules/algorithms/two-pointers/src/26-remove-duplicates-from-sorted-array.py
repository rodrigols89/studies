from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:                          # O(1)
            return 0                          # O(1)
        write = 1                             # O(1)
        for read in range(1, len(nums)):      # O(n)
            if nums[read] != nums[read - 1]:  # O(1)
                nums[write] = nums[read]      # O(1)
                write += 1                    # O(1)
        return write                          # O(1)


if __name__ == '__main__':
    s = Solution()
    arr = [0,0,1,1,1,2,2,3,3,4,9,15]
    k = s.removeDuplicates(arr)
    print("Number of unique elements:", k)
    print("Unique elements:", arr[:k])
