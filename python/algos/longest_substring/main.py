class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [s[0]]
        for ltr in s[1:]:
            if ltr in stack:
                res = len(stack) if len(stack) > res else res
                stack = stack[stack.index(ltr)+1:]
            stack.append(ltr)
        res = len(stack) if len(stack) > res else res
        return res
    
    def __call__(self, s:str):
        return self.lengthOfLongestSubstring(s)
    
longest_substring = Solution()
