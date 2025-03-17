# Problem: 2206. Divide Array Into Equal Pairs (Easy)

# Solution 1: Hashmap

# Time: O(n)
# Space: O(n)

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        
        for count in dic.values():
            if count % 2 == 1:
                return False

        return True