# Problem: 2401. Longest Nice Subarray (medium)

# Solution 1: Sliding Window

# Time: O(n)
# Space: O(1)
# Notes: uses running or to check which bits have been 1 in the window, if there is an overlap during the AND
#        operation, the new number breaks the window and we must shrink using XOR to remove an element.

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        running_or = 0
        ans = 0
        for right in range(len(nums)):
            while running_or & nums[right] != 0:
                running_or ^= nums[left]
                left += 1
            
            running_or |= nums[right]
            ans = max(ans, right - left + 1)
        
        return ans
