class Solution:
    def reverse(self, x: int) -> int:
        ans = int(''.join([i for i in str(x) if i.isnumeric()])[::-1])
        if ans.bit_length() >= 32:
            return 0
        if not str(x)[0].isnumeric():
            return int(str(x)[0] + str(ans))
        return ans
        
    def __call__(self, x:int):
        return self.reverse(x)
    
reverse_interger = Solution()
