class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                continue
            else:
                nums[i]*=2
                nums[i+1]=0

        zeros_count = nums.count(0)
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        for j in range(i, n):
            nums[j] = 0  

        return nums
