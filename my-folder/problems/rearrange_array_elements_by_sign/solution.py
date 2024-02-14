class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        merged = []
        for i in range(int(len(nums) / 2)):
            merged.append(pos[i])
            merged.append(neg[i])
        return merged