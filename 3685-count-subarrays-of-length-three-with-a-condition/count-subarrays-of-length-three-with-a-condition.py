class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums) - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]

            if first + third == middle / 2:
                count += 1
        return count