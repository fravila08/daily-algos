class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

    def __call__(self, x: int):
        return self.isPalindrome(x)
    
palindrome = Solution()