# Problem: 2594. Minimum Time to Repair Cars

# Efficient solution notes:
# - This is an optimization problem, but that doesn't mean we should immediately use DP. Using DP state
#   representation like dp[mechanic][car] would take O(n * cars), which is too slow.
# - Large Constraints -> DP sucks
# - Prefer binary search, two pointer, greedy

# Solution 1: Brute Force

# Time: O(n * cars)
# Space: O(n)
# Notes: rejected by TLE

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ans = 0
        num_cars = [0] * len(ranks)
        curr_times = [0] * len(ranks)
        for _ in range(cars):
            min_new_time = float('inf')
            min_index = 0
            for i in range(len(ranks)):
                new_time = (num_cars[i] + 1) ** 2 * ranks[i]
                if new_time < min_new_time:
                    min_new_time = new_time
                    min_index = i
            num_cars[min_index] += 1
            curr_times[min_index] = num_cars[min_index] ** 2 * ranks[min_index]
            ans = max(curr_times)
            print(_, min_index)
        
        return ans

# Solution 2: Binary Search on optimal time

# Time: O(n + max_rank * log(max_rank))
# Space: O(n) -> used by freq array
# Notes: Binary search on smallest possible time: set low to 1 and high to maxRank * cars^2, keep searching until 
#        low == high, at which point you are sure to have found the smallest time possible.

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        maxRank = max(ranks)
        freq = [0] * (maxRank + 1)
        for rank in ranks:
            freq[rank] += 1
        
        high = maxRank * cars * cars
        low = 1
        while low < high:
            mid = (low + high) // 2
            carsRepaired = 0
            for rank in range(1, maxRank + 1):
                carsRepaired += freq[rank] * floor(sqrt(mid // rank))
            
            if carsRepaired >= cars:
                high = mid
            else:
                low = mid + 1

        return low

            

