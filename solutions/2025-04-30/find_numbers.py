# Problem: 1295. Find Numbers with Even Number of Digits (Easy)

# Solution 1: Iteration

# Time: O(n)
# Space: O(1)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
            
        return count
