
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_len = len(nums)
        """
        Something I didn't realize until really thinking about it, is that there
        is no need to iterate through the entire list in the first for loop.
        1. If an answer isn't found where there's only two numbers left, than the
           problem would have no answer.
        2. If there wasn't an answer found and I iterated to the final index,
           the second for loop would fail because the +1 would cause jdx to fall
           out of index.
        """
        for idx in range(nums_len-1):
            for jdx in range(idx+1, nums_len):
                if nums[idx] + nums[jdx] == target:
                    return [idx, jdx]

    def __call__(self, x, y):
        return self.twoSum(x, y)


twoSum = Solution()