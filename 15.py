class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Solution 1

        # base case
        if len(nums) < 3:
            return []

        res = []
        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and n == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                
                threesum = n + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
