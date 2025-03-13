# PROBLEM: 3356. Zero Array Transformation II

# Solution 1: Brute force

# Time: O(len(nums) * len(queries))
# Space: O(1)
# Notes: solution rejected by TLE

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def allZero(array):
            for num in array:
                if num != 0:
                    return False
            return True

        if allZero(nums):
            return 0
            
        steps = 0
        for query in queries:
            for i in range(query[0], query[1] + 1):
                nums[i] -= min(nums[i], query[2])
            steps += 1
            if allZero(nums):
                break
        return steps if allZero(nums) else -1

# Solution 2: Line Sweep Algorithm

# Time: O(len(nums) + len(queries)) -> we iterate through nums once and queries once
# Space: O(N) -> used by difference_array
# Notes: Intuition is that for each num in nums, we check if the processed queries seen so far are enough to 
#        reduce num to zero using a difference_array and a total_sum representing the prefix sum of the 
#        difference_array. 

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        # k holds number of queries used (ans)
        k = 0
        # used to specify difference windows for each query
        difference_array = [0] * (n + 1)

        for i in range(n):
            while total_sum + difference_array[i] < nums[i]:
                
                if k + 1 > len(queries):
                    return - 1

                left, right, val = queries[k]
                if right >= i:
                    difference_array[max(left, i)] += val
                    difference_array[right + 1] -= val

                k += 1
            total_sum += difference_array[i]
        
        return k
