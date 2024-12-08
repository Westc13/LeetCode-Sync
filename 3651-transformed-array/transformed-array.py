class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                new_index = (i + nums[i]) % n
                new_index = (new_index + n) % n
                result[i] = nums[new_index]
        return result