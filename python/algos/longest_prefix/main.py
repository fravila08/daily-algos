class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        for idx in range(len(strs[0])):
            for word in strs[1:]:
                if idx == len(word) or word[idx] != strs[0][idx]:
                    return res
            res += strs[0][idx]
        return res
    
    def __call__(self, x: list[str]):
        return self.longestCommonPrefix(x)
    
longestPrefix = Solution()
