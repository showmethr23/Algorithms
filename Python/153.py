class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Solution 1
        # Binary search

        l, r = 0, len(nums) -1
        res = nums[0]
        
        while l < r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l+r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res
        