# Problem: 3394. Check if Grid can be Cut into Sections (Medium)

# Solution 1: sorting

# Time: O(n log n)
# Space: O(1)

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def checkValidCutsAxis(n, rectangles, axis):
            start_index = 0 if axis == 'x' else 1
            end_index = 2 if axis == 'x' else 3
            rectangles.sort(key=lambda rectangle: rectangle[start_index])
            cuts = 0
            last_end = 0
            for rectangle in rectangles:
                if rectangle[start_index] >= last_end and last_end != 0:
                    # rectangle starts at same time or after previous
                    cuts += 1
                    if cuts >= 2:
                        return True

                last_end = max(last_end, rectangle[end_index])
                
            return False

        return checkValidCutsAxis(n, rectangles, 'x') or checkValidCutsAxis(n, rectangles, 'y')

        