# Problem: 2780. Minimum Index of a Valid Split (Medium)

# Solution 1: Hash Table

# Time: O(n)
# Space: O(n)

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        dominant_element = 0
        for key, val in count.items():
            if val > (len(nums) // 2):
                dominant_element = key
        
        if len(nums) % 2 == 1 and count[dominant_element] == len(nums) // 2 + 1:
            return -1

        dominant_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant_element:
                dominant_count += 1
                if dominant_count > (i + 1) // 2:
                    return i

        return -1
