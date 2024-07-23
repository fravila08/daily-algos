class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        rows = ['' for _ in range(numRows)]
        row_idx = 0
        increasing = True
        for ltr in s:
            rows[row_idx] +=ltr
            if row_idx == 0 or row_idx == numRows - 1:
                increasing = False if row_idx else True
            row_idx = row_idx + 1 if increasing else row_idx -1
        return ''.join(rows)

    def __call__(self, s:str, numRows:int):
        return self.convert(s, numRows)

zigzag_convert = Solution()

