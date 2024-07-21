"""
A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
```
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
```
"""


class IsSquare:
    def __init__(self, n) -> None:
        self.num: int = n

    """
    The easiest answer I was able to come up with was
    iterating through a list of the numbers leading up
    to our number squaring it and comparing it.

    this works for most scenarios but it has a huge problem
    in space and time complexity
    """

    def simple_is_square(self) -> bool:
        if self.num < 0:
            return False
        for n in list(range(0 if not self.num % 2 else 1, self.num + 1, 2)):
            if n**2 == self.num:
                return True
            if n**2 > self.num:
                return False

    """
    After doing a bit of research I found the 
    Babylonian Algorithm which was pretty cool but 
    hard to interpret into code.

    This solution had a much stronger Big-O rating
    and was able to work with larger numbers more
    efficiently.
    """

    def babylonian_is_square(self) -> bool:
        if self.num < 0:
            return False
        if self.num == 0:
            return True
        mid = self.num // 2
        used = set([mid])
        while mid**2 != self.num:
            mid = (mid + (self.num // mid)) // 2
            if mid in used:
                return False
            used.add(mid)
        return True

    """
    Upon doing a quick google search of the actual problem 
    to see if I may have missed anything I found that Python
    just like you can square integers utilizing the `**` operator,
    you can also find if something has a square root squaring it by .5
    """

    def easy_is_square(self) -> bool:
        return self.num > -1 and self.num**0.5 % 1 == 0
