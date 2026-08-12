class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) != (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple
        if negative:
            quotient = -quotient
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX
        return quotient