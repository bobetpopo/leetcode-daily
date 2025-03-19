# Problem: 3191. Minimum Operations to Make Binary Array Elements Equal to One I (medium)

# Time: O(n)
# Space: O(1)
# Notes: Seemed difficult at first, but the problem is easy once you realize if you want to flip a 0 bit and all
#        the preceding bits are 1, you can only flip the 0 and the next two bits, or you will have to break 
#        the preceding order

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            elif i + 2 < len(nums):
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
            else:
                return -1
        return ans
        

        