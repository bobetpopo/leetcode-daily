# Problem: 2033. Minimum Operations to Make a Uni-Value Grid (Medium)

# Solution 1: sorting

# Time: O(n log n)
# Space: O(n)
# Notes: We are given a grid, but it is helpful to realize the grid is unnecessary and you can turn it into an 
#          array problem. Once we make sure that it is possible to make a uni-value grid using increments or 
#          decrements of x, it suffices to find the middle element and count the steps to make everything middle.


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)
        for i in range(1, len(nums)):   
            diff = nums[i] - nums[i - 1]
            if diff % x != 0:
                return -1
        
        nums.sort()
        mid = nums[len(nums) // 2]
        ans = 0
        for num in nums:
            ans += abs(num - mid) // x

        return ans